#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from setuptools import setup, find_packages
 
__version__ = '1.0.1'

min_numpy_ver = '1.7.0'

setup(
 
    name='fastga',
    version=__version__,

    author='The FastGA team',

    license="Unlicense",
 
    packages=find_packages(),
 
    description="Implementation of the so-called Heavy-Tailed Mutation Operator",
 
    long_description=open('README.rst').read(),
 
    install_requires=["numpy >= {}".format(min_numpy_ver)],
 
    # Active la prise en compte du fichier MANIFEST.in
    include_package_data=True,
 
    # Une url qui pointe vers la page officielle de votre lib
    url='https://github.com/FastGA/fast-genetic-algorithms',
 
    # Il est d'usage de mettre quelques metadata à propos de sa lib
    # Pour que les robots puissent facilement la classer.
    # La liste des marqueurs autorisées est longue:
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers.
    #
    # Il n'y a pas vraiment de règle pour le contenu. Chacun fait un peu
    # comme il le sent. Il y en a qui ne mettent rien.
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "License :: Public Domain",
        "Programming Language :: Python :: 3.5",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
    ],
)
