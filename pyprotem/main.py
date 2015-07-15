#!/usr/bin/env python
# -*- coding: ascii -*-

r"""
pyProTem acts as a temporary project for the time being to test tox, travis, futurize, etc.

<Paragraph description see docstrings at http://www.python.org/dev/peps/pep-0257/>
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


pyProTem
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

"""

# for multi-file projects see LICENSE file for authorship info
# for single file projects, insert following information
__author__ = 'Charlie Taylor'
__copyright__ = 'Copyright (c) 2015 Charlie Taylor'
__license__ = 'GPL-3'
__version__ = '0.1.1' #Versioning: http://www.python.org/dev/peps/pep-0386/
__email__ = "charlietaylor@users.sourceforge.net"
__status__ = "Development" # "Prototype", "Development", or "Production"

#
# import statements here. (built-in first, then 3rd party, then yours)
#
# Code goes below.
# Adjust docstrings to suite your taste/requirements.
#

class ProTem(object):
    """pyProTem acts as a temporary project for the time being to test tox, travis, futurize, etc.

    Longer class information....
    Longer class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.

        eggs: An integer count of the eggs we have laid.
    """

    def __init__(self):
        """Inits ProTem with blah."""
        self.likes_spam = True
        self.eggs = 3

    def public_method(self, arg1, arg2, mykey=True):
        """Performs operation blah.
        
        :param arg1: description of arg1
        :param arg2: description of arg2
        :type arg1: int
        :type arg2: float
        :keyword mykey: a needed input
        :type mykey: boolean
        :return: None
        :rtype: None
        
        .. seealso:: blabla see stuff
        
        .. note:: blabla noteworthy stuff
        
        .. warning:: blabla arg2 must be non-zero.
        
        .. todo:: blabla  lots to do
        """
        pass

if __name__ == '__main__':
    C = ProTem()
