#!/usr/bin/env python
from setuptools import setup, find_packages
import os
import glob
version = None

with open(
        os.path.join(os.path.dirname(__file__),
                     'dockerwrapper/version.py')) as version_file:
    exec(version_file.read())

requirements = [
    'PyYaml',
    'pyconfigmanager',
]

dependency_links = [
    """git+https://github.com/miacro/pyconfigmanager.git\
@master#egg=pyconfigmanager-9999"""
]


def get_scripts():
    result = []
    for item in glob.glob(
            os.path.join(os.path.dirname(__file__), "dockerwrapper/bin/*")):
        if os.access(item, os.X_OK):
            result.append(item)
    return result


def get_package_data():
    pattern = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "dockerwrapper",
        "*.yaml")
    return glob.glob(pattern)


long_description = ''
setup(
    name='dockerwrapper',
    version=version,
    description='dockerwrapper',
    long_description=long_description,
    url='',
    author='miacro',
    author_email='fqguozhou@gmail.com',
    maintainer='miacro',
    maintainer_email='fqguozhou@gmail.com',
    packages=find_packages(exclude=['test.*', 'test', 'tests.*', 'tests']),
    install_requires=requirements,
    classifiers=[
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
    ],
    scripts=get_scripts(),
    ext_modules=[],
    package_data={'dockerwrapper': get_package_data()},
    dependency_links=dependency_links,
)
