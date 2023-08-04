import json

filename = 'veriyi_saklamak\\uygulama\\jsons\\kullanici_verisi.json'

with open(filename) as f:
    fav_number = json.load(f)
    print("ı know your favourite number! It's " + str(fav_number) + ".")
    