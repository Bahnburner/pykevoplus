from setuptools import setup
import os

setup(
    name = "pykevoplusnew",
    version = "3.0.",
    author = "Dominick Meglio",
    author_email = "dmeglio@gmail.com",
    description = "Control Kwikset Kevo locks",
    license = "MIT",
    keywords = "kevo kwikset",
    packages = ["pykevoplusnew"],
    url = "https://github.com/dcmeglio/pykevoplus",
    long_description = open(os.path.join(os.path.dirname(__file__), "README.rst")).read(),
    install_requires = [
        "requests",
        "beautifulsoup4"
    ]
)
