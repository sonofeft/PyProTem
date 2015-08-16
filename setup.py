"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/pyprotem
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

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
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

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        "Intended Audience :: End Users/Desktop",

        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    platforms='any',

    # What does your project relate to?
    keywords='pyprotem setuptools development tox travisci nose nosetests',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    
    packages=find_packages(exclude=['.tox', '.hg', 'docs']),
    #package_dir = {'pyprotem':''},
    
    include_package_data = True,

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    #install_requires=[
    #    "requests>=1.0",
    #    "quantum-gravity>=1.0",
    #    "unobtanium>=0.4",
    #],
    install_requires=['future'],

    tests_require=['nose','coverage'],
    test_suite='tests', # allows "setup.py test" to work

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    #extras_require={
    #    'dev': ['check-manifest'],
    #    'test': ['coverage'],
    #},
    
    zip_safe= False,

    # If there are data files included in your packages that need to be
    # installed, use MANIFEST.in to specify them, NOT package_data
    # >>>>> USE MANIFEST.in, NOT package_data <<<<<< NOTE <<<<<<<<
    #package_data={
    #    'pyprotem': ['package_data.dat'],
    #},

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    #data_files=[('my_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.

    # If installing from source, then
    # the best way to install PyProTem is to use pip after navigating to the source directory

    #     cd <path to where setup.py is located>
    #     pip install -e .
        
    # This will execute the setup.py file and insure that its pip-specific commands are run.
    
    #entry_points={
    #    'console_scripts': [
    #        'pyprotem=pyprotem.main:main',
    #    ],
    #},
)