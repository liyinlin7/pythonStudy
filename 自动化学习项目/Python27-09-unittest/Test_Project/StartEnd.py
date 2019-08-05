import unittest


class Setup_tearDown(unittest.TestCase):
    def setUp(self):
        print("test start")

    def tearDown(self):
        print("test end")
