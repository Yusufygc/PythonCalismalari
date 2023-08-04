import json

def get_stored_username():
    """Eğer kullanıcı adı varsa onu getir."""
    filename = 'veriyi_saklamak\\kullanici_veris.json'
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
    filename = 'veriyi_saklamak\\kullanici_verisi_yeni.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    
def greet_user():
    """kullanıcıyı selamla."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()