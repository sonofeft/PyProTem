.. project_layout


Project Layout
==============

.. _Read the docs: http://readthedocs.org/
.. _Sphinx: http://sphinx.pocoo.org/
.. _reStructuredText: http://sphinx.pocoo.org/rest.html

.. _Travis CI: http://docs.travis-ci.com
.. _GitHub: https://github.com/
.. _tox automation: https://testrun.org/tox/latest/
.. _PyPy: http://pypy.org/

PyProTem acts as a temporary project to test tox, travis, futurize, etc. using GitHub for source code control.

The PyProTem project layout is shown below::

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


Use PyProTem to test `tox automation`_ usage locally and `Travis CI`_ on GitHub_. The goal is to operate with python 2, 3 and PyPy_.

tk_nosy.py is included as a helper tool that watches local files, detects changes and runs nosetests when changes are detected.  For Test Driven Development (TDD), this is a desirable workflow.

The documentation of PyProTem is hosted on `Read the docs`_.  It is created by Sphinx_ using reStructuredText_ and linked to the GitHub repository.  Whenever the RST files change on GitHub, the docs are updated on `Read the docs`_.


Test Discovery
--------------

Because of the layout, the unit tests need to be told the path to the pyprotem/ directory.

Test discovery between nosetests and py.test seemed to be different with Travis CI.  

With nosetests, it was enough to add to the search path at the beginning of the unittest file::

    sys.path.append(os.path.abspath("../"))
    
With py.test it was necessary to add::

    sys.path.append(os.path.abspath("."))
    
So now to be independent of testing software I add both at the beginning::

    import sys, os
    sys.path.append(os.path.abspath("."))
    sys.path.append(os.path.abspath("../"))


