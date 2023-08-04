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


class Admin(Kullanıcı):
    def __init__(self, first_name, last_name, age,gender, password):
        super().__init__(first_name, last_name, age, gender, password)
        #self.privileges=["can add post","can delete post","can ban user"],
        self.privileges=Privileges(["can add post","can delete post","can ban user"])

    #def show_privileges(self):
    #    print(f"admin's privileges are : {self.privileges}")

# nitelikleri farklı bir class olarak tanımlayıp bu classı Admin sınıfı içinde kullandık

class Privileges:
    def __init__(self,privileges):
        self.privileges=privileges

    def show_privileges(self):
        print(f"admin's privileges are : {self.privileges}")


administor = Admin("yusuf","yağcı",21, "male","ysfygc__pitonsever")
administor.greeting()
administor.describe_person()
administor.privileges.show_privileges()