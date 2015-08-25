"""A setuptools based setup module.

Find the documentation at: http://pyprotem.readthedocs.org/en/latest/
Find the source code at:   https://github.com/sonofeft/PyProTem

"""

# Always prefer setuptools over distutils
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyprotem',

    version = '0.1.7',  # METADATA_RESET:    version = '<<version>>',

    description='PyProTem acts as a temporary project for the time being to test tox, travis, futurize, etc.',
    long_description=long_description,

    # The project's main homepage.
    url='http://pyprotem.readthedocs.org/en/latest/',
    download_url='https://github.com/sonofeft/PyProTem',

    # Author details
    author='Charlie Taylor',
    author_email='cet@appliedpython.com',

    # license
    license='GPL-3',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
        "Intended Audience :: End Users/Desktop",
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    platforms='any',
    keywords='pyprotem setuptools development tox travisci nose nosetests',

    packages=find_packages(exclude=['.tox', '.hg', 'docs']),
    include_package_data = True,

    # List run-time dependencies here.  These will be installed by pip when
    install_requires=['future'],

    tests_require=['nose','coverage'],
    test_suite='pyprotem.tests', # allows "setup.py test" to work
    zip_safe= False,
)