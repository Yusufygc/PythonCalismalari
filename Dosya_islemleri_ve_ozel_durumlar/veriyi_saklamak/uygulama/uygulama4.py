import json

def get_stored_username():
    """Eğer kullanıcı adı varsa onu getir."""
    filename = 'veriyi_saklamak\\uygulama\\jsons\\kullanici_adi.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_username():
    """Yeni kullanıcı adı sor."""
    username = input("What is your name? ")
    filename = 'veriyi_saklamak\\uygulama\\jsons\\kullanici_adi.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    
def greet_user():
    """kullanıcıyı selamla."""
    username = get_stored_username()
    print("son kullanıcı adi : " ,username)
    cevap = input("kullanıcı adınız doğru mu? (e/h) :")
    if cevap == "e":
        print(f"Welcome back, {username}!")
    elif cevap == "h":
        username = get_new_username()
        print("We'll remember you when you come back!")
    else:
        print("yanlış giriş yaptınız")
        greet_user()

greet_user()