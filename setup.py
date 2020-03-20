# -*- coding: utf-8 -*-
"""
documentation
"""

from setuptools import setup, find_packages

setup(
    name='pilyso_io_omero',
    version='0.0.1.dev1',
    description='pilyso - image reading library - omero reader',
    long_description='Python Image anaLYsis SOftware library',
    author='Christian Sachs',
    author_email='c.sachs@fz-juelich.de',
    url='',
    packages=find_packages(),
    requires=['numpy'],
    license='GPL',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GPL License',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Scientific/Engineering :: Bio-Informatics',

    ]
)