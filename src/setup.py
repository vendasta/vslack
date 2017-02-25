import os
from setuptools import setup

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'vslack', 'VERSION')) as f:
    version = f.read().strip()

setup(
    name="vslack",
    version=version,
    packages=["vslack"],
    url="https://github.com/vendasta/VA-vslack.git",
    description="Vendasta Slack library",
    package_data={
        'vslack': ['VERSION', 'README.md']
    },
    install_requires=[]
)
