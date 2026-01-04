# File: setup.py
# File Created: Friday, 18th March 2022 4:24:10 pm
# Author: Philippe Hawi (hawi@usc.edu)

from setuptools import setup, find_packages
from setuptools.command.install import install
import platform
import os

description = "Probabilistic Learning on Manifolds (Legacy code)"


dependencies = [
    "numpy",
    "matplotlib",
    "scipy",
    "joblib"
]


# Additional utility scripts
scripts = ["scripts/plom_run.py", "scripts/plom_make_input_template.py"]


# Platform-specific shared libraries
system = platform.system()
if system == "Windows":
    shared_libs = [
        "lib/potential_eigen.dll",
        "lib/potential_native.dll"
    ]
elif system == "Linux":
    shared_libs = [
        "lib/potential_eigen.so",
        "lib/potential_native.so"
    ]
else:
    shared_libs = []


# Setup function
setup(
    name="plom-legacy",
    version="0.7.0",
    description=description,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/philippe-hawi/PLoM-Legacy",
    author="Philippe Hawi",
    author_email="hawi@usc.edu",
    license="MIT",
    install_requires=dependencies,
    packages=find_packages(),  # Automatically finds all packages with __init__.py
    package_data={"plom_legacy": shared_libs},
    scripts=scripts,
    python_requires=">=3.6",
)
