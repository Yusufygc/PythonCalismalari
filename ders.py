
# ad =int(input("lütfen adınızı giriniz:"))
# # float ile for içinde döndürülemez
# print(ad)

# print(type(ad))


# for i in (ad):
#     print(i)

# % bu ifade moddur


print(4%3)
# kullanıcı tarafından girilen herhangi bir sayının  
# mükkemmel sayı olup olmadığını bize göstercek kod
# mük sayı = bölenleri toplamı kendine eşit olan sayı 
"""
sayı = int(input("bir sayı giriniz :"))

toplam = 0

for i in range(1,sayı):
    if sayı % i == 0 :
        toplam = toplam + i
        if toplam == sayı:
            print("bu sayı mükkemmel sayıdır.")
        else:
            print("bu sayı mükkemmel falan değildir.")
"""    
# hatam 2.if i de for altında yazmak.        
"""           
sayı = int(input("bir sayı giriniz :"))

toplam = 0

for i in range(1,sayı):
    if sayı % i == 0 :
        toplam = toplam + i
if toplam == sayı:
    print("bu sayı mükkemmel sayıdır.")
else:
    print("bu sayı mükkemmel değildir.")
""" 



