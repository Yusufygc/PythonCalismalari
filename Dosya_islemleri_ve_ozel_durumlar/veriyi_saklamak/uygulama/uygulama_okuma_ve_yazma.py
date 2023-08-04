import json

def get_stored_number():
    """Eğer sayı varsa onu getir."""
    filename = 'veriyi_saklamak\\uygulama\\jsons\\kullanici_verisi.json'
    try:
        with open(filename) as f:
            fav_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return fav_number
    
def get_new_number():
    """Yeni sayı sor."""
    filename = 'veriyi_saklamak\\uygulama\\jsons\\kullanici_verisi.json'
    fav_number = input("What is your favourite number? ")
    with open(filename, 'w') as f:
        json.dump(fav_number, f)

def greet_user():
    """kullanıcıyı selamla."""
    fav_number = get_stored_number()
    if fav_number:
        print("ı know your favourite number! It's " + str(fav_number) + ".")
    else:
        fav_number = get_new_number()
        print("oookey that is your fav number, " + str(fav_number) + "!")

greet_user()