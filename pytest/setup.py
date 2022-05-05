import unittest


class TestRepetitiveCode(unittest.TestCase):
  def setUp(self):
  self.var = -10
def test_absolute(self):
  self.assertEqual(self.var, -10)
def test_overwrite(self):
  self.assertTrue(self.var < 0)
if __name__ == "__main__":
  unittest.main()