from distutils.core import setup

setup(
    name="brittle_wit",
    version="0.0.2",
    author="John Bjorn Nelson",
    author_email="jbn@pathdependent.com",
    packages=["brittle_wit",],
    keywords=["twitter"],
    license="MIT",
    description="An async Twitter library for Python.",
    long_description=open("README.md").read(),
    url="https://github.com/jbn/BrittleWit",
    package_data={"brittle_wit": ["api_reference.json"]},
    include_package_data=True,
)
