##################################################################################################
"""
class Dog:
    def  __init__(self ,name ,age) -> None:
        self.name= name
        self.age = age

    def sit(self):
        print(f"{self.name} now sitting")

    def roll_over(self):
        print(f"{self.name} rollovered")


my_dog = Dog("garabaş",5)

print(f"benim köpeğimin adı {my_dog.name} ")
print(f"benim köpeğimin yaşı {my_dog.age} ")

my_dog.sit()
my_dog.roll_over()

######

your_dog=Dog("kıllı",6)

print(f"senin köpeğinin adı {your_dog.name} ")
print(f"senin köpeğinin yaşı {your_dog.age} ")

your_dog.sit()
your_dog.roll_over()
"""
##################################################################################################
"""
class Restorant:
    def __init__(self,restoran_adı,mutfak_türü):
        self.restoran_adı=restoran_adı
        self.mutfak_türü=mutfak_türü

    def restoran_calisma(self):
        print("restoran açıktır")

    
    def restoran_tanimla(self):
        print(f"restoranın adı : {self.restoran_adı}")
        print(f"restoranın mutfak kültürü : {self.mutfak_türü}")

    
restorant = Restorant("Hacıların kebap","TÜRRRKK mutfağı")

restorant.restoran_calisma()
restorant.restoran_tanimla()


restorant1 = Restorant("tatlıcı memoli","TÜRRRKK mutfağı")
restorant2 = Restorant("le'oeka mabpale","fransız mutfağı")
restorant3 = Restorant("suri","arrap mutfağı")


restorant1.restoran_tanimla()
restorant2.restoran_tanimla()
restorant3.restoran_tanimla()

"""
##################################################################################################
"""
class Kullanıcı:
    def __init__(self,first_name,last_name,age,gender,password):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.gender=gender
        self.pasword=password

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
"""











