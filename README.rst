
.. image:: https://travis-ci.org/sonofeft/PyProTem.svg?branch=master
    :target: https://travis-ci.org/sonofeft/PyProTem

.. image:: https://img.shields.io/pypi/v/PyProTem.svg
    :target: https://pypi.python.org/pypi/pyprotem
        
.. image:: https://img.shields.io/pypi/pyversions/PyProTem.svg
    :target: https://wiki.python.org/moin/Python2orPython3

.. image:: https://img.shields.io/pypi/l/PyProTem.svg
    :target: https://pypi.python.org/pypi/pyprotem


PyProTem
========

PyProTem acts as a temporary project to test tox, travis, futurize, etc.

Testing the layout shown below::

    MyProject/
        myproject/
            __init__.py
            mycode.py
            examples/
                example_1.py
            tests/
                __init__.py
                test_mycode.py
        docs/
            conf.py
            index.rst
        LICENSE.txt
        MANIFEST.in
        README.rst
        requirements.txt
        setup.cfg
        setup.py
        tk_nosy.py
        tox.ini

Use pyProTem to test tox usage locally, travis CI on GitHub on checkin, tk_nosy to watch files locally and alert breakage, operation under both python 2 and 3.
