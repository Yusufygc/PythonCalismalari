"""
with open('dosya_okuma_islemi\\pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
"""
# Satır satır okuma
"""
filename = 'dosya_okuma_islemi\\pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip() )
"""
# dosyadan satırlar listesi oluşturma
"""
filename = 'dosya_okuma_islemi\\pi_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines()

for line in lines:
    print(line.rstrip())
    
print(lines)
"""
#dosyanın içeriği ile çalışmak
"""
filename = 'dosya_okuma_islemi\\pi_digits.txt'

with open(filename) as file_object:
    lines=file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
"""
# büyük dosyalarla çalışmak
"""
filename = 'dosya_okuma_islemi\\pi_milyon_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
print(f"{pi_string[:52]}...")
print(len(pi_string))
"""
# doğum günü pi sayısında var mı?
"""
filename = 'dosya_okuma_islemi\\pi_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthay = input("Doğum gününüzü giriniz (ay/gün/yıl): ")
if birthay in pi_string:
    print("Doğum gününüz pi sayısında var.")
else:
    print("Doğum gününüz pi sayısında yok.")
"""







