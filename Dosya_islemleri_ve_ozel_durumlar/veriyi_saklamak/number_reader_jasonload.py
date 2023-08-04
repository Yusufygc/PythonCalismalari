import json

filename = 'veriyi_saklamak\\numbers.json'

with open(filename) as f:
    numbers = json.load(f)

print(numbers)