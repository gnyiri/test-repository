import unittest
from teamcity import is_running_under_teamcity
from teamcity.unittestpy import TeamcityTestRunner


class Test1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTest1Tc1(self):
        self.assertTrue(False)

    def testTest1Tc2(self):
        self.assertTrue(False)

    def testTest1Tc3(self):
        self.assertTrue(True)

    def testTest1Tc4(self):
        self.assertTrue(True)

    def testTest1Tc5(self):
        self.assertTrue(True)

    def testTest1Tc6(self):
        self.assertTrue(True)


if __name__ == '__main__':
    if is_running_under_teamcity():
        runner = TeamcityTestRunner()
    else:
        runner = unittest.TextTestRunner()
    unittest.main(testRunner=runner)
