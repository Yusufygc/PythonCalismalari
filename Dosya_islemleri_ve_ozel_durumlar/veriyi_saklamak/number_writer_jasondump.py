# JSON.DUMP() VE JSON.LOAD() KULLANARAK VERİYİ SAKLAMAK

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'veriyi_saklamak\\numbers.json'

with open(filename, 'w') as f:
    json.dump(numbers, f)