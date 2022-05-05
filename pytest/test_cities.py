import unittest
from city_functions import city_country


class CityTestCase(unittest.TestCase):
    """Tests for 'city_functions.city_country' function."""

    def test_city_country(self):
        result = city_country('london', 'england')
        self.assertEqual(result, 'London, England')

unittest.main()