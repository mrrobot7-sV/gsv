import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "nmap_gsv",
    version = "0.1",
    author = "John Abraham",
    author_email = "pdv.dev07@outlook.com",
    description = "Get nmap service info-command from nmap scanned XML-file.",
    long_description_content_type = 'text/markdown',
    license = "GPLv3+",
    keywords = "nmap parser",
    python_requires='>=3',
    url = "https://github.com/mrrobot7-sV/nmap-gsv",
    packages=['nmap_gsv_mrrobot7-sV'],
    long_description=read('README.md'),
    install_requires=['python-libnmap>=0.7.3'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    ]
)