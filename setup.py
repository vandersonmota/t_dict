#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    'jsonpointer==1.4',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='t_dict',
    version='0.1.1',
    description='Traversing and Querying Dicts the easy way',
    long_description=readme + '\n\n' + history,
    author='Vanderson Mota',
    author_email='vanderson.mota@gmail.com',
    url='https://github.com/vandersonmota/t_dict',
    packages=[
        't_dict',
    ],
    package_dir={'t_dict':
                 't_dict'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='t_dict',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
