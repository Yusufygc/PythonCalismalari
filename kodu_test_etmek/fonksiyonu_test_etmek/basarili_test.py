import unittest
from name_func import get_name

class NamesTestCase(unittest.TestCase):
    """name_func.py test"""
    def test_first_last_name(self):
        """Is 'Janis Joplin' working?"""
        formatted_name = get_name('janis','joplin') # ,'john'
        self.assertEqual(formatted_name,'Janis Joplin') # ,'Janis John Joplin' bu şekilde opsiyonel isimde eklenip kontrol edilebilir.ya da yeni fonkisyon yazılır.

    def test_first_middle_last_name(self):
        """Is 'Wolfgang Amadeus Mozart' working?"""
        formatted_name = get_name('wolfgang','mozart','amadeus')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()