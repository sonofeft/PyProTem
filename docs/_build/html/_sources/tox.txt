.. tox

tox automation
==============

.. _tox: https://tox.readthedocs.org/en/latest/



tox_ automates and standardizes testing in Python.  It is great because it will test many different python versions on Windows and Linux (CPython-2.6, 2.7, 3.3, 3.4, Jython, pypy, etc.).  For python code aiming to support python 2 and 3 on Windows and Linux it is an excellent approach.

My workflow is to develop on Windows, run tox_ there and when satisfied, push to GitHub which automatically runs :ref:`internal_travis_ci` on Linux (i.e. :ref:`internal_travis_ci` runs different versions of python on Linux machines). This approach verifies python 2 and 3 on Windows and Linux.

If not already intalled, then install tox_ with ``pip install tox`` or perhaps ``sudo apt-get install python-tox`` on Linux.

``pip`` is likely already on you system, however, if not see :ref:`internal_pip_installation`

On Linux
--------

On Linux a simple tox.ini file should work such as::

    # content of: tox.ini , put in same dir as setup.py
    [tox]
    envlist = py26,py27
    [testenv]
    deps=pytest       # install pytest in the venvs
    commands=py.test  # or 'nosetests' or ...

On Windows
----------

On Windows 8 I had more fiddling around to do, but still had good luck with the following tox.ini file::

    # content of: tox.ini , put in same dir as setup.py
    [tox]
    envlist = py27,py34
    setenv =
        PYTHONPATH = C:\python34
        PATH = C:\python34;C:\python34\Scripts

    [testenv]
    deps=pytest       # PYPI package providing py.test
    commands=py.test  # or 'nosetests' or ...

    # python25 may not work... ONLY worked on virtual XP machine (so far)
    [testenv:py25]
    basepython=D:\TOX\python25\python.exe

    [testenv:py26]
    basepython=D:\TOX\python26\python.exe

    [testenv:py27]
    basepython=D:\TOX\python27\python.exe

    [testenv:py32]
    basepython=D:\TOX\python32\python.exe

    [testenv:py33]
    basepython=D:\TOX\python33\python.exe

    [testenv:py34]
    basepython=C:\python34\python.exe


    [testenv:pypy3]
    basepython=D:\TOX\pypy3-2.4.0-win32\pypy.exe

    [testenv:pypy]
    basepython=D:\TOX\pypy-2.6.0-win32\pypy.exe



