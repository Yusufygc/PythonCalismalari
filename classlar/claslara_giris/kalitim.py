"""
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading=0

    def isim_ata(self):
        long_name= f"{self.make} {self.model} {self.year}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"arabanın kilometre durumu : {self.odometer_reading}")

    def update_odometer(self,km):
        self.odometer_reading=km

    def increase_odometer(self,km):
        self.odometer_reading += km


class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size=75

    def describe_battery(self,battery_size=75):
        self.battery_size =battery_size 
        print(f"bu arabanın bataryası {self.battery_size} kWh tir")

    def isim_ata(self):
        long_name= f"{self.make} {self.model} {self.year}"
        return long_name.upper()
    
my_tesla=ElectricCar("tesla","model s",2019)
print(my_tesla.isim_ata())
my_tesla.describe_battery(95)
"""
##########################################################
# üst sınıftaki metodları geçersiz kılmak
# bunu yapmak için alt sınıfın içinde üst sınıfta gçersiz kılmak istediğimiz metodla aynı isimde bir metod tanımlamamız gerekir
"""
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading=0

    def isim_ata(self):
        long_name= f"{self.make} {self.model} {self.year}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"arabanın kilometre durumu : {self.odometer_reading}")

    def update_odometer(self,km):
        self.odometer_reading=km

    def increase_odometer(self,km):
        self.odometer_reading += km

    def fill_gas_tank(self):
        print(f"{self.model} benzinle çalışır")


class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size=75

    def describe_battery(self,battery_size=75):
        self.battery_size =battery_size 
        print(f"bu arabanın bataryası {self.battery_size} kWh tir")

    def isim_ata(self):
        long_name= f"{self.make} {self.model} {self.year}"
        return long_name.upper()
    
    def fill_gas_tank(self):
        print(f"{self.model} benzinle çalışmaz çünkü elektrikle çalışır")
    
my_tesla=ElectricCar("tesla","model s",2019)
print(my_tesla.isim_ata())
my_tesla.describe_battery(95)

my_tesla.fill_gas_tank()

my_honda=Car("honda","civic",2019)

my_honda.fill_gas_tank()
"""
##########################################################
# nitelikleri class şeklinde gruplandırmak ve sınıf içinde tanımlamak
"""
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading=0

    def isim_ata(self):
        long_name= f"{self.make} {self.model} {self.year}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"arabanın kilometre durumu : {self.odometer_reading}")

    def update_odometer(self,km):
        self.odometer_reading=km

    def increase_odometer(self,km):
        self.odometer_reading += km

    def fill_gas_tank(self):
        print(f"{self.model} benzinle çalışır")


class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Batery() ###### burada batery sınıfını çağırdık

    def isim_ata(self):
        long_name= f"{self.make} {self.model} {self.year}"
        return long_name.upper()
    
    def fill_gas_tank(self):
        print(f"{self.model} benzinle çalışmaz çünkü elektrikle çalışır")

class Batery:
    def __init__(self,battery_size=75):
        self.battery_size=battery_size

    def describe_battery(self,battery_size):
        self.battery_size =battery_size
        print(f"bu arabanın bataryası {self.battery_size} kWh tir")

    def get_range(self):
        if self.battery_size == 75:
            range=260
            print(f"bu araba {self.battery_size} kwh ile {range} km gider")
        elif self.battery_size == 100:
            range=315
            print(f"bu araba {self.battery_size} kwh ile {range} km gider")
        else:
            print("bu arabanın bataryası 75 veya 100 kwh değil")


my_tesla=ElectricCar("tesla","model s",2019)
print(my_tesla.isim_ata())
my_tesla.battery.describe_battery(100)
my_tesla.battery.get_range()
"""

##########################################################