# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = '''
This package contains the tikz Sphinx extension, which enables the use
of the PGF/TikZ LaTeX package to draw nice pictures.
'''

requires = ['Sphinx>=0.6']

setup(
    name='sphinxcontrib-tikz',
    version='0.4',
    url='http://bitbucket.org/birkenfeld/sphinx-contrib',
    download_url='http://pypi.python.org/pypi/sphinxcontrib-tikz',
    license='BSD',
    author='Christoph Reller',
    author_email='creller@ee.ethz.ch',
    description='Sphinx "tikz" extension',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
    use_2to3 = True,
)
