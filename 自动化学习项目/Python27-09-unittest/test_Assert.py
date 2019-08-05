from calculator import Math
import unittest


class TestMath(unittest.TestCase):
    def setUp(self):
        print("test start")

    def test_add(self):
        j = Math(5, 10)
        self.assertEqual(j.add(), 15)

    def test_add1(self):
        j = Math(5, 10)
        self.assertNotEqual(j.add(), 12)

    def test_asserIs(self):
        self.assertIs("wang", "wang")

    def test_asserIn(self):
        self.assertIn("w", "wang")

    def tearDown(self):
        print("test end")
