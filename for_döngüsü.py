############## FOR DÖNGÜSÜ ##############
#########################################
"""
kvp = ["Polat","Memati","abdülhey","erhan"]

for kv in kvp:
    print(kv)

for kv in kvp:
    print(f"{kv.upper()},sevdiğim karakterlerdendir.")
    print(f"Bir sonraki operasyonu heyecanla bekliyorum {kv.title()} bey\n") 
    # \n bunu en sona eklersek satırdan sonra boşluk bırakır başa koyarsak üsten boşluk bırakır .
"""
##########################################
"""
pizza = ["sucuklu","mantarsız","turco"]

for x in pizza:
    print(x)
    print(f"{x} pepperoni pizzayı severim.")

print(f"{pizza[0]} pizzayı,\n {pizza[1]} pizzayı,\n {pizza[2]} pizzayı ,\nnasıl olursa olsun pizzayı gerçekten severim ")
 
"""  
# print(f"""
#    {pizza[0]} pizzayı,
#     {pizza[1]} pizzayı,
#     {pizza[2]} pizzayı,
#     nasıl olursa olsun pizzayı gerçekten severim """)


##########################################
"""
kedi = ["tekir","british","aslan","puma"]
for a in kedi: 
    print(f"{a} güzel yaratıktır")

print("bu hayvanların hepsi çok güzel hayvanlardır.SEVERİZ")
"""
##########################################
"""
for value in range(1,5):
    print(value)

for a in range(6):
    print(a)

numbers = list(range(1,7))
print(numbers)

even_numbers = list(range(2,35,3)) # 3.parametre sayım aralığını belirler
print(even_numbers)


squares = []

for value in range(1,11):
    square = value**2
    squares.append(square)
    
print(squares)

# ÜSTTEKİNİN KISA YOLU

squares = []

for value in range(1,11):
    squares.append(value**2)
    
print(squares)

squares = [value**2 for value in range(1,11)] # HESAPLANMIŞ LİSTE = AYNI İŞİ TEK SATIRDA YAPABİLMEMİZİ SAĞLAR
print(squares)

"""
##########################################
"""
sayı = [1,2,4,5,6,9,8]

print(min(sayı))
print(max(sayı))
print(sum(sayı))
"""
##########################################
# BASİT FOR UYGULAMALARI
##########################################
"""
for iplikci_nedim in range(1,21):
    print(iplikci_nedim,"dolarcik caniim.")
"""
########################
"""
sayı = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in sayı:
    print(i,".sayı")
"""
########################
"""
for i in range(1,20,2):
   print(i)
"""
########################
"""
list =[3,6,39,12,15,18,21,24,27,30]

for ucerli in list:
    print(ucerli)
"""
########################  
"""
for küp in range(1,11):
    a=küp**3 
    print(a)     

kupler = [sayı**3 for küp in range(1,11)]
print(kupler)
"""
##########################################
# FOR DÖGÜSÜ İLE LİSTELERLE ÇALIŞMAK
"""
players = ["dominic","letty","brian","roman","tej","khan"]
print(players[0:4])
print(players[2:5])
print(players[:3])
print(players[2:])
print(players[-3:])
print(players[-2:])


print("Başrol oyuncular :")
for i in players[:3]:
    print(i.title())

sayı = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(sayı[0:16:2]) # 1 DEN 15 E KADAR 2 ŞER ATLAYARAK YAZDIRIR.
"""
#####################
"""
list = ["ali","veli","merve","remzi","ece"]
print("ilk üç öğe şunlardır : ")
print(list[0:3])

print("ortadaki üç öğe şunlardır : ")
print(list[1:4])

print("son üç öğe şunlardır : ")
print(list[-3:])

drinks_menu = ["kola","ayran","şerbet","gazoz","maden_suyu"]

other_drinks_menu = drinks_menu[:]

print(drinks_menu)
print(other_drinks_menu)

drinks_menu.append("çay")
other_drinks_menu.append("enerji içeceği")
other_drinks_menu.append("hoşaf")


print("İlk menüdekiler :")
for i in drinks_menu:
    print(i)


print("İkinci menüdekiler :") 
for a in other_drinks_menu:
    print(a)
"""
##########################################

