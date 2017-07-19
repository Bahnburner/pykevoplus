from setuptools import setup
import os

setup(
    name = "pykevoplus3",
    version = "1.0.1",
    author = "Tristan Caulfield",
    author_email = "tcaulfld@gmail.com",
    description = "Control Kwikset Kevo locks",
    license = "MIT",
    keywords = "kevo kwikset",
    packages = ["pykevoplus3"],
    url = "https://github.com/bahnburner/pykevoplus3",
    long_description = open(os.path.join(os.path.dirname(__file__), "README.rst")).read(),
    install_requires = [
        "requests",
        "beautifulsoup4"
    ]
)
