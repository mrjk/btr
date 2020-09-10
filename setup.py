
from setuptools import setup

version='0.1'

setup(
    name='behavox-test-rcordier',
    version=version,
    author='Robin Cordier',
    author_email='robin.cordier@gmail.com',
    description='This is an recruitment test for behavox',
    zip_safe=False,
    packages=['btr'],
    install_requires=[
        "click>=7.1",
        "PyYAML>=5.3",
    ],
    entry_points = {
        'console_scripts':
        [
            'btr=btr.cli:cli',
        ]
    },
)
