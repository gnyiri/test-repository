import unittest
from teamcity import is_running_under_teamcity
from teamcity.unittestpy import TeamcityTestRunner


class Test2(unittest.TestCase):

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

    def testTest2Tc1(self):
        self.assertEqual(1, 0)
        self.assertEqual(0, 1)
        self.assertEqual(1, 1)
        self.assertEqual(0, 0)


if __name__ == '__main__':
    if is_running_under_teamcity():
        runner = TeamcityTestRunner()
    else:
        runner = unittest.TextTestRunner()
    unittest.main(testRunner=runner)

