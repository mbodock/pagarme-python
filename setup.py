# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import pagarme

requires = [i.strip() for i in open("requirements.txt").readlines()]

testing_extras = [
    'pytest',
    'pytest-cov',
]

setup(
    name='pagarme-python',
    version=pagarme.__version__,
    author='Allisson Azevedo',
    author_email='allisson@gmail.com',
    packages=find_packages(),
    license='MIT',
    description=pagarme.__description__,
    long_description=pagarme.__long_description__,
    url='https://github.com/pagarme/pagarme-python',
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
    tests_require=['pytest'],
    extras_require={
        'testing': testing_extras,
    },
)
