from random import randint
class Die:
    """Bir zarı temsil eden bir sınıf"""

    def __init__(self, num_sides=6):
        """Varsayılan olarak 6 yüzlü bir zar oluşturun"""
        self.num_sides = num_sides

    def roll(self):
        """1 ve zarın yüz sayısı arasında rastgele bir sayı döndürün"""
        return randint(1, self.num_sides)
    
zar = Die(20) # sayıları değiştirerek deneyin

print(zar.roll())