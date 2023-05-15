##################################### KISIM-2 --> BÖLÜM-1) LİSTELER ################
"""
kalem = ["tükenmez", "dolma","kurşun","renkli","simli"]
#print(kalem)

#print(kalem[2]) # İSTEDĞİN ELEMANIN İNDEKS NUMARASI YAZ ÇEK

#print(kalem[3].upper()) # bu şekilde varklı fonksiyonlar kullanıp liste içindeki elemanları değiştirebiliriz

#print(kalem[-1]) # SONDAKİ ELEMANI YAZDIRIR -2 -3 -4 de sondaki elemanlı yazdırır

#message = f"kullanmaktan en keyim aldığım kalem {kalem[0].upper()} kalemdir."
#print(message)
"""
##########################################################
"""
sayi = [ 1,2,3,4,5]

toplam = kalem + sayi

print(toplam)
"""
#######################################################33
"""
del kalem[2]

print(kalem)
 
del sayi[4]

print(sayi)
"""
############################################
"""
kalem.append("pahalı")

print(kalem)

sayi.append(6)

print(sayi)
"""
############################################
"""
kalem.insert(2,"ucuz kalem")

print(kalem)

sayi.insert(3,56)

print(sayi)
"""
############################################
"""
toplam.pop(3)
print(toplam)

kalem.pop(3)

print(kalem)
"""
############################################
"""
sayi.remove(2)
sayi.remove(3)
sayi.remove(6)
print(sayi)

yeni = [ 1,7,1,11,34,5,4,2,3,9,0,1,1]

yeni.remove(1)

print(yeni)
"""
############################################
"""
yeni.sort()

print(yeni)

kalem.sort()
print(kalem)
"""
############################################
"""
kalem.reverse()
print(kalem)

toplam.reverse()
print(toplam)
"""
############################################
"""
yeni = [ 1,7,1,11,34,5,4,2,3,9,0,1,1]
v=yeni.count(1)
print(v)

names = ["elif","ayça","ekrem","ayşenur","dilara"]

print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

b=f" Selamün aleyküm {names[4]} nabersin "

print(b)
"""
############################################
"""
cars = ["BMW","AUDI","MERCEDES","ANADOL"]

#cars[0]="tofaş"  liste elemanını değiştirmek istiyorsan eğer bu şekilde yapabilirsin
print(cars)

cars.append("EGEA")

print(cars)

actors =[]
actors.append("burak özçelik")
actors.append("burak özçivit")
actors.append("kıvanç tatlıtuğ")
actors.append("NECATİ ŞAŞMAZ")

actors.insert(0,"çağatay ulusoy")
actors.insert(3,"ganyotçu")
print(actors)

#del actors[2]
#del actors[::] hepsini sildim
#del actors[:-2]
#del actors[-2:]

popped_actors = actors.pop()

print(actors)
print(popped_actors)

# listenin içinden tamamen silmek istiyorsan del , listeden çıkarmak istiyorsan pop , inddeksini değilde değerini bilindiğin bir şeyi silmek istiyprsan remove
"""
############################################
"""
# UFAK BİR LİSTE ÇALIŞMASIYDI 

yemek_davet =["fatih","yavuz","attila"]

print(f"\tsayın atalarım {yemek_davet[0]},{yemek_davet[1]},{yemek_davet[2]} bu akşamki yemek davetimde sizi ağırlamaktan onur duyarım")
print(f"\tne yazık ki {yemek_davet[2]} han'nın katılamayacağını yeni öğrenmenin derin teessüfü içerisindeyim. ")

yemek_davet[2]= " baybars han"

print(f"\tattila hanımızın yerine ulu hakan{yemek_davet[2]}'ı aramızda ağırlamaktan şeref duyarım")

a= "tarihimizin sizler gibi büyük insanlara sahiplik yapması bize çok büyük gurur veriyor "
b="hepiniz toyumuza hoş geldiniz."

print(f"\tHer biri birbirinden kıymetli {yemek_davet[0]},{yemek_davet[1]},{yemek_davet[2]}\n\t{a}\n\t{b} ")

print("\tToyumuza katilmak üzere yola çıkan 3 misafirmiz daha vardır")

yemek_davet.insert(0,"sultan alparslan")
yemek_davet.insert(3,"vezir tonyukuk")
yemek_davet.append("nizamımülk")

kisiler= yemek_davet

print(f"\tHer biri birbirinden kıymetli {kisiler[0]},{kisiler[1]},{kisiler[2]},{kisiler[3]},{kisiler[4]},{kisiler[5]}\n\t{a}\n\t{b} ")

print("\tsayın atalar kusura bakmayın we are going to just two person")

kisiler.pop()
print("\tsayın nizamımülk yediğimiz halttan dolayı özür dileriz")
kisiler.pop()
print("\tsayın baybars han yediğimiz halttan dolayı özür dileriz")
kisiler.pop()
print("\tsayın vezir tonyukuk yediğimiz halttan dolayı özür dileriz")
kisiler.pop()
print("\tsayın yavuz yediğimiz halttan dolayı özür dileriz")
print("\tsultan alparslan ve sultan fatih we choosed you for dinner if you join us,we'll be so happy sir ")

#del kisiler[::]

v=len(kisiler)

print(f"{v} kişi davet ettim")
"""
##############################################
"""
iller = ["kayseri","sakarya","istanbul","manisa","bursa","samsun"]

#iller.sort()

#print(iller)

#iller.sort(reverse=True)

#print(iller)

print("İşte orjinal liste:")
print(iller)
print("işte sıralanmış liste :")
print(sorted(iller))
print("tekrardan orjinal liste:")
print(iller)

iller.reverse()
print(iller)

iller.reverse()
print(iller)

print(len(iller))
"""
##############################################
"""
istek = ["amerika","italya","ispanya","türkistan","japonya"]

print(istek)
print(sorted(istek))
print(istek)

print(sorted(istek,reverse=True))
print(istek)

istek.reverse()
print(istek)

istek.reverse()
print(istek)

istek.sort()
print(istek)
istek.sort(reverse=True)
print(istek)
"""
##############################################
"""
iller = ["kayseri","sakarya","istanbul","manisa","bursa","samsun"]

print(iller[6])
# KASITLI İNDEKS HATASI. AYIK OL İNDEKS HATASI YAPMA
"""
##############################################



























































































































