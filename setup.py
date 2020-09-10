
from setuptools import setup

version='0.1'

setup(
    name='click-project',
    version=version,
    author='Robin Cordier',
    author_email='robin.cordier@gmail.com',
    description='This is an recruitment test',
    zip_safe=False,
    install_requires=[
        "click>=7.1",
    ],
    entry_points = {
        'console_scripts':
        [
            'btr=btr.cli:cli',
        ]
    },
)
