# Standard Library
import os

# Third-Party
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), "README.md"), encoding="utf-8") as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="EASGen-Remastered",
    packages=["EASGen"],
    version="0.1.14.1",
    description="A Python library to generate EAS SAME Audio using Raw Data - Remastered",
    author="secludedhusky",
    author_email="secludedhusky@chesbaycommunications.com",
    license="ODbL-1.0",
    install_requires=["EASGen"],
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Newton-Communications/EG",
    keywords="audio sound eas alerting emergency-alert-system",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: Other/Proprietary License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
)
