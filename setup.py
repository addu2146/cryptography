# setup.py

from setuptools import setup, find_packages

setup(
    name="adduciphers",       # this is the pip name
    version="0.1.0",
    packages=find_packages(), # finds your adduciphers package
    python_requires=">=3.7",
)
