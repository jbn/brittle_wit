from distutils.core import setup

setup(
    name="brittle_wit",
    version="0.0.1",
    packages=["brittle_wit",],
    license="MIT",
    long_description=open("README.md").read(),
    package_data={"brittle_wit": ["api_reference.json"]},
    include_package_data=True,
)
