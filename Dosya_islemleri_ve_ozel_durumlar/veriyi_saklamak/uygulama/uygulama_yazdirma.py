import json

fav_number = int(input("What is your favourite number? "))

filename = 'veriyi_saklamak\\uygulama\\jsons\\kullanici_verisi.json'

with open(filename, 'w') as f:
    json.dump(fav_number, f)
    print(f"Well that's a great number maann, {fav_number}!")