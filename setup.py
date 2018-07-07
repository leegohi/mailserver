#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup,find_packages
except ImportError:
    from distutils.core import setup,find_packages

settings = dict()


# Publish Helper.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

settings.update(
    name='mailserver',
    version='1.0',
    description='SMTP for auto register',
    author='walle',
    author_email='walle88@qq.com',
    url='https://github.com/leegohi',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mailserver = mailserver.main:main',
        ],
    },
    install_requires=['logbook', 'argparse'],
    license='BSD',
    classifiers=(
        # 'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    )
)


setup(**settings)
