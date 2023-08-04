import unittest
from isci_uyg import Employee

class TestEmployee(unittest.TestCase):
    """Employee sınıfının testi"""
    def setUp(self):
        """Tüm test metodları için bir işçi oluşturur"""
        self.my_employee = Employee("Ali","Yılmaz",10000)

    def test_give_default_raise(self):
        """Varsayılan zam miktarının doğru şekilde verilip verilmediğini test eder"""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary,15000)

    def test_give_custom_raise(self):
        """Belirli bir zam miktarının doğru şekilde verilip verilmediğini test eder"""
        self.my_employee.give_raise(10000)
        self.assertEqual(self.my_employee.salary,20000)

if __name__ == '__main__':
    unittest.main()