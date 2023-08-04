import json

username = input("What is your name? ")

filename = 'veriyi_saklamak\\kullanici_verisi.json'

with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")