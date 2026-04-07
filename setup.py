"""Setup configuration for hello_python package."""

from setuptools import setup, find_packages

setup(
    name="hello_python",
    version="1.0.0",
    description="Hello Python CI test project",
    py_modules=["main"],
    packages=find_packages(),
    python_requires=">=3.7",
)
