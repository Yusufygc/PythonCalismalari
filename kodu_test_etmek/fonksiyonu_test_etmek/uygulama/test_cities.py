import unittest
from city_function import get_city_country

class CityCountryTestCase(unittest.TestCase):
    """city_function.py test"""
    def test_city_country(self):
        """Is 'Santiago,Chile' working?"""
        formatted_name = get_city_country('santiago','chile')
        self.assertEqual(formatted_name,'Santiago Chile')
    
    def test_city_country_population(self):
        """Is 'Santiago,Chile - population =5000000' working?"""
        formatted_name = get_city_country('santiago','chile','5000000')
        self.assertEqual(formatted_name,'Santiago Chile - Population =5000000')

if __name__ == '__main__':
    unittest.main()