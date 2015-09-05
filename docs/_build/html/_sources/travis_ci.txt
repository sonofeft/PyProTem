.. travis_ci

.. _internal_travis_ci:

Travis CI
=========


Turning on the Travis CI Switch
-------------------------------

I had trouble finding the right location to turn on Travis CI for the GitHub project.

.. _Travis CI Getting Started: http://docs.travis-ci.com/user/getting-started/

.. _Sign in to Travis CI: https://travis-ci.org/

I started at the `Travis CI Getting Started`_ page, followed by signing into Travis CI at `Sign in to Travis CI`_

After fumbling around and getting signed in, I got to the "Settings" option for my project and flipped the buttons to "ON" for running a build on pushes and pulls using my .travis.yml file.


My baseline .travis.yml file seemed to work just fine::

    language: python
    python:
        - "2.7"
        - "pypy"
        - "3.3"
        - "3.4"

    install:
        - pip install -r requirements.txt
    script:
        - py.test
    
I recieved an email after synching the file with GitHub that the above tests were successfully run.

Test Discovery Wrinkle
----------------------

The only wrinkle was a difference in test discovery between nosetests and py.test.  The directory in which the test file executes appears to be different between the two.

With nosetests, it was enough to add to the search path at the beginning of the unittest file::

    sys.path.append(os.path.abspath("../"))
    
With py.test it was necessary to add::

    sys.path.append(os.path.abspath("."))
    
So now to be independent of testing software I add both at the beginning::

    import sys, os
    sys.path.append(os.path.abspath("."))
    sys.path.append(os.path.abspath("../"))

