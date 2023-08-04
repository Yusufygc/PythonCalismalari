########################################################################################
"""
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def isim_ata(self):
        long_name= f"{self.make} {self.model} {self.year}"
        return long_name.title()
    
my_new_car = Car("audi","a4",2019)
print(my_new_car.isim_ata())
"""
########################################################################################
# niteliğe varsayılan değer atama
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


my_new_car = Car("audi","a4",2019)
print(my_new_car.isim_ata())
my_new_car.read_odometer()
"""
########################################################################################
# nitelik değerlerini değiştirmek
# bir niteliği doğrudan değiştirmek
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


my_new_car = Car("audi","a4",2019)
print(my_new_car.isim_ata())

my_new_car.odometer_reading=23
my_new_car.read_odometer()
"""
########################################################################################
# bir niteliği fonksiyon ile değiştirmek
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


my_new_car = Car("audi","a4",2019)
print(my_new_car.isim_ata())

my_new_car.update_odometer(55)
my_new_car.read_odometer()
"""
#########################################################
# çıtır bir müdahale "kilometre sayacını düşüremezsiniz!"
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
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("kilometre sayacını düşüremezsiniz!")


my_new_car = Car("audi","a4",2019)
print(my_new_car.isim_ata())

my_new_car.update_odometer(55)
my_new_car.read_odometer()
"""
########################################################################################
# niteliği metot ile arttırmak
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


ikinci_el_araba = Car("subaru","outback",2015)
print(ikinci_el_araba.isim_ata())

ikinci_el_araba.update_odometer(23500)
ikinci_el_araba.read_odometer()

ikinci_el_araba.increase_odometer(100)
ikinci_el_araba.read_odometer()
"""
########################################################################################
# uygulama
"""
class Restorant:
    def __init__(self,restoran_adı,mutfak_türü):
        self.restoran_adı=restoran_adı
        self.mutfak_türü=mutfak_türü
        self.servis_sayısı=0


    def servis_sayısını_güncelle(self,servis):
        self.servis_sayısı=servis
        print(f"servis sayısı {self.servis_sayısı} olarak güncellendi")
    
    def servis_yapılan_müşteri_sayısı(self,servis):
        self.servis_sayısı += servis
        print(f"servis yapılan müşteri sayısı {self.servis_sayısı} olarak güncellendi") 

    def servis_yapılan_müşteri_sayısı_artır(self,servis):
        self.servis_sayısı += servis
        print(f"servis yapılan müşteri sayısı {self.servis_sayısı} olarak güncellendi")
        

    
    def restoran_tanimla(self):
        print(f"restoranın adı : {self.restoran_adı}")
        print(f"restoranın mutfak kültürü : {self.mutfak_türü}")

    
restorant = Restorant("Hacıların kebap","TÜRRRKK mutfağı")
restorant.servis_sayısını_güncelle(38)

restorant.servis_yapılan_müşteri_sayısı(25)

restorant.servis_yapılan_müşteri_sayısı_artır(10)
"""
########################################################################################
# uygulama 2
"""
class Kullanıcı:
    def __init__(self,first_name,last_name,age,gender,password):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.gender=gender
        self.pasword=password
        self.login_attempts=0

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"giriş denemesi sayısı {self.login_attempts} olarak güncellendi")

    def reset_login_attempts(self):
        self.login_attempts=0
        print(f"giriş denemesi sayısı {self.login_attempts} olarak güncellendi")

    def greeting(self):
        print(f"helloo {self.first_name +' '+ self.last_name}")


    def describe_person(self):
        print(f"User's name is : {self.first_name +' '+  self.last_name}")
        print(f"User's age is : {self.age}")
        print(f"User's gender is : {self.gender}")
        print(f"User's pasword is : {self.pasword}")
        
user = Kullanıcı("yusuf","yağcı",21,"male","ysfygc__pitonsever")

user.greeting()
user.describe_person()

user.increment_login_attempts()
user.increment_login_attempts()

user.reset_login_attempts()
"""










