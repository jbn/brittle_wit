import os
import re
import textwrap
from collections import defaultdict


def pep8_join(tokens, sep, init_indent='', next_indent='    ', tail_k=0):
    """
    Join a sequence of tokens for PEP8-compliant code generation.

    :param tokens: an iterable of tokens
    :param sep: a string separator to delimit the tokens
    :param init_indent: a string for the initial line's indentation
    :param next_indent: a string for all subsequent lines' indentation
    :param tail_k: subtracted from 79 to get the maximum line length
    """
    return textwrap.fill(sep.join(str(tok) for tok in tokens),
                         width=79 - tail_k,
                         initial_indent=init_indent,
                         break_long_words=False,
                         subsequent_indent=next_indent,
                         drop_whitespace=True)


RESERVED_WORDS = {'False', 'None', 'True', 'and', 'as', 'assert', 'break',
                  'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
                  'finally', 'for', 'from', 'global', 'if', 'import', 'in',
                  'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
                  'return', 'try', 'while', 'with', 'yield'}


def _param_name_translations(param_names):
    """
    :return: a dict from the original name to the source-safe
        name.
    """
    translations = {}
    for k in param_names:
        name = k

        name = name.replace(':', '_').replace('[]', '')

        if name in RESERVED_WORDS:
            name += '_'

        assert name.isidentifier()

        translations[k] = name

    return translations


def _generate_def_line(api_def, method_name_in_fname=False, **renamings):
    name = _generate_func_name(api_def, method_name_in_fname)
    declaration = "def {}(".format(name)

    tokens = [renamings.get(k, k) + ("={}".format(default) if default else "")
              for k, default in _generate_param_tokens(api_def)]
    if not tokens:
        return declaration + "):"

    return pep8_join(tokens,
                     ", ",
                     init_indent=declaration,
                     next_indent=len(declaration) * " ",
                     tail_k=2) + "):"


def _generate_param_doc(param_def, name):
    desc, kind = param_def.get('description'), param_def.get('type')

    # There is no additional documentation for this argument, so
    # don't document it more than the implicit function defition.
    if not desc and not kind:
        return None

    desc = desc or ""

    if kind:
        desc += " ({})".format(kind)

    doc_str = ":param {}: {}".format(name, desc)

    return textwrap.fill(doc_str, width=79,
                         initial_indent="    ",
                         subsequent_indent="        ",
                         replace_whitespace=True,
                         break_long_words=False)


def _generate_doc_str(api_def, **renamings):
    desc_line = textwrap.fill(api_def['desc'] or "",
                              width=79,
                              initial_indent='    ',
                              subsequent_indent='    ',
                              replace_whitespace=True,
                              break_long_words=False)

    param_docs = []
    for param_def in api_def['params']:
        k = param_def['name']
        s = _generate_param_doc(param_def, renamings.get(k, k))
        if s:
            param_docs.append(s)
    param_doc = "\n\n" + "\n\n".join(param_docs) if param_docs else ''

    doc = "\n".join([desc_line]) + param_doc

    return '    """\n' + doc + '\n    """'


def _generate_binding(api_def, **renamings):
    s = "    binding = {"
    indent = len(s) * " "

    bindings = []
    for param in api_def['params']:
        name = param['name']
        binding = "'{}': {}".format(name, renamings.get(name, name))
        bindings.append(binding)
    if not bindings:
        return s + "}"

    bindings = pep8_join(bindings,
                         sep=", ",
                         init_indent=s,
                         next_indent=indent,
                         tail_k=1)

    return bindings + "}"


def _generate_url_block(api_def):
    lines = ["    url = '{}'".format(api_def['url'])]

    if api_def['slugs']:
        lines.append("    url = url.format(**binding)")

    return "\n".join(lines)


REQ_TEMPLATE = "    " + """
    return TwitterRequest('{method}',
                          url,
                          '{family}',
                          '{service}',
                          binding)
""".strip()


def _generate_req_str(api_def):
    return REQ_TEMPLATE.format(**api_def)


def generate_source(api_def, use_http_method=False):
    param_names = [d['name'] for d in api_def['params']]
    renamings = _param_name_translations(param_names)

    def_line = _generate_def_line(api_def,
                                  method_name_in_fname=use_http_method,
                                  **renamings)
    doc_str = _generate_doc_str(api_def, **renamings)
    binding_str = _generate_binding(api_def, **renamings)
    url_str = _generate_url_block(api_def)
    ret_str = _generate_req_str(api_def)

    return "\n".join([def_line, doc_str, binding_str, url_str, ret_str])


AUTOGEN_HEADER = '''
###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################
'''.strip()


def generate_modules(base_dir, definitions, func_gen=generate_source):
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
    for group, api_defs in definitions.items():
        for api_def in api_defs:
            family = api_def['family'].split(":")[1]
            paths[group].add(family)
            code_blocks[(group, family)].append(func_gen(api_def))

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
                fp.write("from brittle_wit import TwitterRequest, IGNORE\n\n\n")
                for code_block in code_blocks[group, family]:
                    fp.write(code_block + "\n\n\n")

        import_fmt = "import brittle_wit.{}.{}\n"
        with open(os.path.join(parent_dir, '__init__.py'), "w") as fp:
            fp.write(AUTOGEN_HEADER + "\n\n")

            for family in families:
                fp.write(import_fmt.format(parent_module, family))


def _generate_param_tokens(api_def):
    """
    Generate the function's parameter tokens.

    :param api_def: an api definition.
    """
    params = api_def.get('params')

    if not params:
        return []

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
    tokens = [(param['name'], None) for param in list(reversed(slugged)) + required]

    if optional:
        tokens.append(('*', None))

    # Optionals are keyword-only to protect fail loudly.
    for param in optional:
        tokens.append((param['name'], 'IGNORE'))

    return tokens


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


def _partition_path(path, known_params, slugs):
    namespaces, placeholders = [], []

    for part in path.split("/"):
        if part.startswith(':'):
            k = part[1:]
            assert k in known_params, k
            placeholders.append(k)
            assert k in slugs
        else:
            namespaces.append(part)

    return namespaces, placeholders


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
    namespaces, placeholders = _partition_path(path, known_params,
                                               api_def['slugs'])

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

    # XXX
    if not f_name.isidentifier():
        f_name = "".join(c for c in f_name if c.isidentifier())

    assert f_name.isidentifier(), f_name
    assert f_name, f_name

    return f_name
