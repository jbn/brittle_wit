import os
import re
import textwrap
from collections import defaultdict


def _generate_doc_str(api_def, line_width=79, indent_width=4):
    line_width -= indent_width
    indent = " " * indent_width

    lines = textwrap.wrap(api_def.get('desc') or "", line_width) + [""]

    for param in api_def['params']:
        desc, kind = param.get('description'), param.get('type')

        # No reason to document what is implicit in function arguments.
        if not desc and not kind:
            continue

        name = param['name']
        desc += " ({})".format(param['required'])

        first_line = ":param {}: ".format(name)
        j = line_width - len(first_line)
        first_line += desc[:j]
        desc = desc[j:]
        lines.append(first_line)

        indent = " " * indent_width
        for paragraph in desc.splitlines():
            wrapped = textwrap.wrap(paragraph,
                                    line_width - indent_width,
                                    replace_whitespace=True)
            for line in wrapped:
                lines.append(indent + line.strip())
            lines.append("")

        lines.append('')

    doc_str = ("\n" + indent).join(lines)
    return indent + doc_str.replace('’', "'").strip()


FUNCTION_TEMPLATE = '''def {name}({arg_str}):
    """
{doc_str}
    """
    url = "{url}"
    {url_formatter}return TwitterRequest('{method}',
                          url,
                          '{family}',
                          '{service}'{binding})

'''

BINDING_INDENT = "                          "


def _generate_formatter(api_def):
    if not api_def['slugs']:
        return ''
    slugs = reversed(api_def['slugs'])
    sp = '                     '
    bindings = (",\n" + sp).join("{}={}".format(s, s) for s in slugs)
    return "url = url.format({})\n    ".format(bindings)


def generate_function_code(defn, name_with_method=False):
    d = {k: defn[k].upper() for k in ['method', 'family', 'service']}
    d['url'] = defn['url']
    d['name'] = _generate_func_name(defn, name_with_method)
    d['doc_str'] = _generate_doc_str(defn)
    d['arg_str'] = _generate_signature_str(defn)
    d['binding'] = ""
    d['url_formatter'] = _generate_formatter(defn)

    if defn['params']:
        d['binding'] += ","

    for param in defn['params']:
        binding_fmt = "\n" + BINDING_INDENT + "{}={}"
        d['binding'] += binding_fmt.format(param['name'], param['name'])

    return FUNCTION_TEMPLATE.format(**d)


AUTOGEN_HEADER = '''
###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################
'''.strip()


def generate_modules(base_dir, definitions, func_gen=generate_function_code):
    """
    Generate the module file skeleton given the definitions.

    - For each group, generate ``{group}_api`` module
    - For each family, generate ``{group}_api.{family}`` module

    :param base_dir: the file directory in which to create the modules
    :param definitions: the extracted api definitions
    :param func_gen: a function that returns a string of generated code
        when given an api_def
    """
    paths, code_blocks = defaultdict(set), defaultdict(list)

    # Gather the paths from the definitions.
    for group, defns in definitions.items():
        for defn in defns:
            family = defn['family'].split(":")[1]
            paths[group].add(family)
            code_blocks[(group, family)].append(func_gen(defn))

    # Create the skeleton.
    for group, families in paths.items():
        # Setup parent module.
        parent_module = group + "_api"
        parent_dir = os.path.join(base_dir, parent_module)
        os.makedirs(parent_dir, exist_ok=True)

        # Write all the definitions.
        for family in families:
            sub_module = os.path.join(parent_dir, family + ".py")
            with open(sub_module, "w") as fp:
                fp.write(AUTOGEN_HEADER + "\n\n\n")
                fp.write("from brittle_wit import TwitterRequest\n\n\n")
                for code_block in code_blocks[group, family]:
                    fp.write(code_block + "\n")

        import_fmt = "import brittle_wit.{}.{}\n"
        with open(os.path.join(parent_dir, '__init__.py'), "w") as fp:
            fp.write(AUTOGEN_HEADER + "\n\n")

            for family in families:
                fp.write(import_fmt.format(parent_module, family))


def _generate_signature_str(api_def):
    """
    Generate the function's signature.

    :param api_def: an api definition.
    """
    params = api_def.get('params')

    if not params:
        return ""

    # Slugs always come first; then required; then optional.
    slugged, required, optional = [], [], []
    for param in params:
        if param['required']:
            if param['name'] in api_def['slugs']:
                slugged.append(param)
            else:
                required.append(param)
        else:
            optional.append(param)

    # Required params come first.
    bindings = [param['name'] for param in list(reversed(slugged)) + required]

    if optional:
        bindings.append('*')

    # Optionals are keyword-only to protect fail loudly.
    for param in optional:
        bindings.append("{}=IGNORE".format(param['name']))

    return ", ".join(bindings)


SLUGS_RE = re.compile(r":[A-Za-z_0-9]+")
SLUG_POSTFIX_RE = re.compile(r"^.*?(:[A-Za-z_0-9]+)$")
SLUG_INFIX_RE = re.compile(r"""^(?:[A-Za-z]*/)?
                               ([A-Za-z0-9_]+)/
                               (\:[A-Za-z_0-9]+)/
                               (.*)$""",
                           re.X)


def _simplify_path(path, family):
    # Special case for some advertising api calls.
    if path.startswith("1/"):
        path = path[2:]
    return path.replace(family, "")


def _generate_func_name(api_def, append_http_method=False):
    """
    Derive a function name from an api_def

    :param append_http_method: if True, then the method name will end
        with ``_via_{HTTP_METHOD}``.
    """
    method = api_def['method']
    family = api_def['family'].split(':')[1]
    path = _simplify_path(api_def['path'], family)

    known_params = {p['name'] for p in api_def['params']}

    if path.startswith('/'):
        path = path[1:]

    # Partition by slug placeholders versus namespaces.
    namespaces, placeholders = [], []
    for part in path.split("/"):
        if part.startswith(':'):
            k = part[1:]
            assert k in known_params, k
            placeholders.append(k)
            assert k in api_def['slugs']
        else:
            namespaces.append(part)

    # I haven't seen more than 2.
    if placeholders:
        f_name = "_".join(namespaces)

        k = len(placeholders)
        if k == 1:
            f_name += "_by_" + placeholders[0]
        elif k == 2:
            b, a = placeholders
            f_name += "_by_{}_and_{}".format(a, b)
        else:
            raise ValueError("Unknown format")
    else:
        f_name = "_".join(namespaces)

    if f_name.startswith('_'):
        f_name = f_name[1:]

    if append_http_method:
        f_name += "_via_" + method.lower()

    if f_name == '':
        f_name = api_def['path']  # Singleton families?

    return f_name
