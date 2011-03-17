#!/usr/bin/env python

from distutils.core import setup


description = "A simple API for counting beans with Flask and Redis."

VERSION = '1.0'

setup(
    name='flask-beans',
    version=VERSION,
    author='Joshua Ourisman',
    author_email='josh@joshourisman.com',
    url='http://github.com/joshourisman/flask-beans',
    description=description,
    long_description=description,
    license='BSD',
    platforms=['any'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        ],
    packages=['beans',],
    install_requires=['flask', 'redis',],
    )