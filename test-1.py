import unittest


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

    def Test1_TC1(self):
        self.assertEqual(1, 0)
        self.assertEqual(0, 1)
        self.assertEqual(1, 1)
        self.assertEqual(0, 0)

if __name__ == '__main__':
    unittest.main()