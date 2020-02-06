import re
from os.path import dirname, join

from setuptools import setup, find_packages


with open(join(dirname(__file__), 'markdownserver', '__init__.py')) as f:
    version = re.match(r'^__version__ = \'(.*)\'', f.read()).group(1)


dependencies = [
    'easycli',
]


setup(
    name='markdown-httpserver',
    version=version,
    url='https://github.com/babakhani/markdown-httpserver',
    author='Reza Babakhani',
    author_email='babakhani.reza@gmail.com',
    description='markdown http server',
    packages=find_packages(),
    install_requires=dependencies,
    license='MIT',
    entry_points={
        'console_scripts': [
            'ms = markdownserver.cli:MarkdownServer.quickstart',
        ]
    }
)
