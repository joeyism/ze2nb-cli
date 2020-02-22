from setuptools import setup, find_packages
from codecs import open
from os import path
import re

here = path.abspath(path.dirname(__file__))

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('ze2nb_cli/__init__.py').read(),
    re.M
    ).group(1)

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
        name = 'ze2nb-cli',
        packages = find_packages(), # this must be the same as the name above
        version = version,
        description = 'A simple CLI for ze2nb',
        long_description = long_description,
        author = 'joeyism',
        author_email = 'joeyism@gmail.com',
        entry_points = {
            "console_scripts": ['ze2nb = ze2nb_cli.cli:main']
        },
        url = 'https://github.com/joeyism/ze2nb-cli', # use the URL to the github repo
        download_url = 'https://github.com/joeyism/ze2nb-cli/archive/{}.tar.gz'.format(version),
        keywords = ['ze2nb', 'cli', 'zeppelin', 'jupyter', 'notebook', 'ipynb', 'note.json'], 
        install_requires = [package.split("\n")[0] for package in open("requirements.txt", "r").readlines()],
        classifiers = [],
        )
