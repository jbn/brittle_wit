from distutils.core import setup

setup(
    name="BrittleWit",
    version="0.1dev",
    packages=["brittle_wit",],
    license="MIT",
    long_description=open("README.md").read(),
    package_data={"brittle_wit": ["api_reference.json"]},
    include_package_data=True,
)
