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

# modülü mdüle aktarmak için import car_1 yazdık sadece car clası olmasını istediğimiz için