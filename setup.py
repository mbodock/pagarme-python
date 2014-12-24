# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import pagarme

version = pagarme.__version__

requires = [
    'requests',
    'httpretty',
]

testing_extras = [
    'nose',
    'coverage',
]

setup(
    name='pagarme-python',
    version=version,
    author='Allisson Azevedo',
    author_email='allisson@gmail.com',
    packages=find_packages(),
    license='MIT',
    description='Pagar.me Python library',
    long_description=open('docs/index.rst').read(),
    url='https://github.com/allisson/pagarme-python',
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'License :: OSI Approved :: MIT License',
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    extras_require={
        'testing': testing_extras,
    },
)
