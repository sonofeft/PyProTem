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

Because of the layout, the unit tests in need to know the path to the pyprotem/ directory in order to import 

