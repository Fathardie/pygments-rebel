#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name='pygments-rebel',
    version='0.1',
    description='Pygments lexer Rebel.',
    long_description=open('README.md').read(),
    keywords='pygments rebel lexer',
    license='BSD',

    author='Sebastiaan la Fleur',
    author_email='sebastiaan@slafleur.nl',

    url='https://github.com/Fathardie/pygments-rebel',

    packages=find_packages(),
    install_requires=['pygments >= 1.4'],

    entry_points='''[pygments.lexers]
                    rebel=pygments_rebel:RebelLexer''',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)