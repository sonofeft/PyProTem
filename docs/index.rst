
.. PyProTem documentation master file, created by
   sphinx-quickstart on Mon Jul 06 00:15:47 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
   
.. image:: https://travis-ci.org/sonofeft/PyProTem.svg?branch=master
    :target: https://travis-ci.org/sonofeft/PyProTem
    
PyProTem
========

PyProTem acts as a temporary project to test tox, travis, futurize, etc.

The layout is shown below::

    PyProTem/
        pyprotem/
            __init__.py
            main.py
        docs/
        tests/
            __init__.py
            test_mycode.py
        LICENSE.txt
        MANIFEST.in
        README.rst
        requirements.txt
        setup.cfg
        setup.py
        tk_nosy.py
        tox.ini

Use PyProTem to test tox usage locally, travis CI on GitHub on checkin, tk_nosy to watch files locally and alert breakage, operation under both python 2 and 3.

Docs and Source
===============

Find the documentation at: `<http://pyprotem.readthedocs.org/en/latest/>`_

Find the source code at: `<https://github.com/sonofeft/PyProTem>`_

Installation From Source
========================

If installing from source, then
the best way to install PyProTem is to use pip after navigating to the directory holding PyProTem::

    cd full/path/to/PyProTem
    pip install -e .
    
    OR on Linux
    sudo pip install -e .
    
    
This will execute the local ``setup.py`` file and insure that the pip-specific commands in ``setup.py`` are run.

May need to install from requirements.txt if the above does not work::

    pip install -r /path/to/requirements.txt


For installing tkinter, I could never get pip to work on Linux, so use the following::

  sudo apt-get install python-tk
  sudo apt-get install python3-tk
  
  sudo apt-get install python-nose
  sudo apt-get install python3-nose
  
Python 3 on Linux
-----------------




Copyright
=========

PyProTem
Copyright (C) 2015  Charlie Taylor

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.


Contents:

.. toctree::
   :maxdepth: 2

   project_layout
   read_the_docs
   tox
   pip
   travis_ci
   fulltable_of_contents
   functions


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


