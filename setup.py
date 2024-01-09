from setuptools import find_packages, setup

def read_requirements(file):
    with open(file) as f:
        return f.read().splitlines()

def read_file(file):
   with open(file) as f:
        return f.read()

long_description = read_file("README.rst")
version = read_file("VERSION")
requirements = read_requirements("requirements.txt")

setup(
    name='pygitlog',
    packages=find_packages(include=['pygitlog']),
    version=version,
    description='Python library for git log summary',
    long_description_content_type = "text/x-rst",  # If this causes a warning, upgrade your setuptools package
    long_description = long_description,
    author='Me',
)