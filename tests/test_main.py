import unittest
# import unittest2 as unittest # for versions of python < 2.7

import sys
sys.path.append("../")
from pyprotem.main import ProTem

class MyTest(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.myclass = ProTem()

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        del( self.myclass )

    def test_should_always_pass_cleanly(self):
        """Should always pass cleanly."""
        pass

    def test_myclass_existence(self):
        """Check that myclass exists"""
        result = self.myclass

        # See if the self.myclass object exists
        self.assertTrue(result)


if __name__ == '__main__':
    # Can test just this file from command prompt
    #  or it can be part of test discovery from nose, unittest, pytest, etc.
    unittest.main()

