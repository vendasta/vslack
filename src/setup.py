import codecs
import os
from setuptools import setup

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'vslack', 'VERSION')) as f:
    version = f.read().strip()

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


setup(
    name="vslack",
    version=version,
    packages=["vslack"],
    url="https://github.com/vendasta/vslack.git",
    description="Vendasta's open source Slack library that makes dealing with incoming webhooks much easier",
    package_data={
        'vslack': ['VERSION', 'README.md']
    },
    license='apache2',
    author='Vendasta Technologies',
    author_email='gholtslander@vendasta.com',
    install_requires=[]
)
