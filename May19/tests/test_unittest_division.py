import unittest
from May19.scripts.division import division


class Tests(unittest.TestCase):
    def test(self):  # test method
        self.assertEqual(division(4, 4), 1)

    def test2(self):  # test method
        self.assertEqual(division(4, -4), -1)

    def test3(self):  # test method
        self.assertTrue(isinstance(division(4, 25), float))