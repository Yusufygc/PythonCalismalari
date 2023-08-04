import json

filename = 'veriyi_saklamak\\kullanici_verisi.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")