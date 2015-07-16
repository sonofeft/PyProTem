.. project_layout


Project Layout
==============

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


