Pyprotem acts as a temporary project for the time being to test tox, travis, futurize, etc.
===========================================================================================

.. image:: https://travis-ci.org/sonofeft/PyProTem.svg?branch=master
    :target: https://travis-ci.org/sonofeft/PyProTem

Testing the layout shown below::

    MyProject/
        myproject/
            __init__.py
            mycode.py
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

Use pyProTem to test tox usage locally, travis CI on GitHub on checkin, tk_nosy to watch files locally and alert breakage, operation under both python 2 and 3.
