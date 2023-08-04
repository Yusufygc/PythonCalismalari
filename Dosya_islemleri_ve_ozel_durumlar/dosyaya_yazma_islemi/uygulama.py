"""
name = input("Adınızı giriniz: ")

with open("dosya.txt", "w") as dosya:
    dosya.write(name)
    dosya.write("\n")


while True:
    name = input("Adınızı giriniz: ")
    if name == "q":
        break
    with open("dosya.txt", "a") as dosya:
        dosya.write(name)
        dosya.write("\n")
"""
    

while True:
    cevap = input("Kodlamayı neden seviyorsunuz: ")
    if cevap == "q":
        break
    with open("dosya.txt", "a") as dosya:
        dosya.write(cevap)
        dosya.write("\n")
        