"""Describe our module distribution to Distutils."""

# Import future modules
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import third-party modules
from setuptools import find_packages
from setuptools import setup

setup(
    name="portable_rez",
    author="longhao",
    author_email="hal.long@outlook.com",
    url="https://github.com/loonghao/portable_rez",
    package_dir={"": "."},
    packages=find_packages("."),
    description="A portable rez.",
    entry_points={},
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)
