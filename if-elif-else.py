
############# CONDITIONAL STATEMENTS (if-elif-else)#############
# FOR İLE LİSTE ELEMANLARINI DOLAŞMAK
"""
cars =["audi","bmw","togg","bentley"]

for i in cars:
    if i == "bmw":         # "=" bu eşitlerken "==" bu, değeri kontrol eder 
        print(i.upper())
    else:
        print(i.title())    
"""
################################################################
"""
# != ---> eşitsizzliği kontrol eder.

istek = "mantar"
if istek != "ançüez":
    print("ançüez istemezüm ha !!")
"""
################################################################
# KULLANICIDAN ALINAN DEĞERİN LİSTEDE OLUP OLMADIĞINI KONTROL ETMEK
"""
A=str(input("isminiz :"))

names = ["ali","veli","cafer"]

if A in names:
    print(f"hoşgeldin {A} kardeş")
else :
    print("daha gelmedi paşa hazretleri")
"""
################################################################
# DEĞİŞKENİN LİSTEDE OLUP OLMADIĞINI KONTROL ETMEK
"""
banlanmış_persons = ["remzi","burak","berke","nalan","fadime"]

user = "abdülhey"

if user not in banlanmış_persons:
    print(f"Sayın {user.upper()} , yorumunuzu yazabilirsiniz.")
"""
################################################################
# KULLANICIDAN ALINAN DEĞERİN ŞARTI SAĞLAYIP SAĞLAMADIĞINI KONTROL ETMEK
"""
vote = int(input("lütfen yaşınızı giriniz :"))

if vote <= 18 :
    print("oy moy veremezssiniz büyüyüp de gelin")
else:
    print("oy namustur kime verdiğine niye verdiğine ayık ol.Allah'a emanet.")    
"""
################################################################
# BİRDEN FAZLA ŞARTI KONTROL ETMEK
# ÇITIR-UYGULAMA : YAŞA GÖRE GİRİŞ ÜCRETİ BELİRLEME
"""
enter =int(input("ödenecek ücret için lütfen yaşınızı giriniz:"))

if enter < 7:
    print("ücretsiz girebilirsiniz")
elif enter <= 18 :
    b = str(input("öğrenci indiriminden faydalanmak için üye olmanız gerekmektedir.üye olmak ister misiniz:"))    
    if b == "evet":
        print("kaydınız başarıyla gerçekleştirilmiştir.15 tl ödeyerek giriş yapabilirsiniz")
    elif b == "hayır" :
        print("ödemeniz gereken miktar 30 TL'dir")

elif enter >= 18:
    print("30 TL ödeyerek giriş yapabilirsiniz")
           
print("iyi eğlenceler dileriz:)")
"""
################################################################
# ŞARTLARA GÖRE PUAN SİSTEMİ BELİRLEMEK(BASİT)
"""
alien = "sarı"

if alien == "yeşil":
    print(" 5 puan kazandınız.")
else:
    print("10 puan kazandınız")


alien = "yeşil"

if alien == "yeşil":
    print(" 5 puan kazandınız.")
else:
    print("10 puan kazandınız")


alien = "kırmızı"

if alien == "yeşil":
    print(" 5 puan kazandınız.")
elif alien == "kırmızı":
    print("20 puan kazandınız")
else:
    print("10 puan kazandınız")
"""
################################################################
# KULLANICI VERİSİNİ ÇOKLU ŞARTLARA GÖRE KONTROL ETMEK
"""
age = int(input("yaşınızı giriniz :"))

if age < 2 :
    print("bu kişi bir bebektir.")
elif age >= 2 and age < 4 :
    print("bu kişi yeni yürümeye başlamış bir çocuktur.")
elif age >= 4 and age < 13 :
    print("bu kişi bir çocuktur.")
elif age >= 13 and age < 20 :
    print("bu yaratık bir ergendir.")  
elif age >= 20 and age < 65 :
    print("bi şahıs bir yetişkindir.")
else:
    print("bu mübarek, yaşlıdır.")                     
"""
################################################################ 
# LİSTEDEKİ ELEMANLARI KONTROL EDİP ŞARTA GÖRE İŞLEM YAPMAK 
"""
istek_listesi = ["mantar","yeşil biber","fazladan peynir"]

for istekler in istek_listesi:
    if istekler == "yeşil biber":
        print("gusura galma elimizde büber yok")
    else:    
        print(f"{istekler} ekleniyor")
    
print("\nPiZZanız hazarlanıyür")    
"""
################################################################  
# LİSTE DOLU MU BOŞ MU KONTROL EDİP ŞARTA GÖRE İŞLEM YAPMAK
"""
istek_listesi = []

if istek_listesi:
    for istekler in istek_listesi:
        print(f"{istekler} ekleniyor")     
    print("pizzanız haziirr")
else:
    print("Malzemesiz pizza istediğinizden emin misiniz? ")    
"""
################################################################
# LİSTELERİ KARŞILAŞTIRIP ŞARTA GÖRE İŞLEM YAPMAK
"""
stokta_olanlar = ["mantar","zeytin","yeşil biber","pepperoni","ananas","fazla peynir"]
istenilen = ["mantar","patates kızartması","fazla peynir"]    
    
for istek in istenilen :
    if istek in stokta_olanlar :
        print(f"{istek} ekleniyor.")
    else :
        print(f"sorry ,{istek} yok.")
print("\nPizzanız hazır!")                
"""    
################################################################ 
# LİSTE DOLU-BOŞ MU KONTROL EDİP ELEMANLARIN ŞARTLARA UYGUNLUĞUNA GÖRE İŞLEM YAPMAK
"""    
names = ["admin","musti","ilayda","semih","ayşe"]    
    
for user in names :
    if user =='admin':
        print("selamünaleyküm admin,durum raporunu görmek ister misin?")
    else :
        print(f"merhaba {user}, tekrar oturum açtığın için teşekkürler.")        
    
    
if names == []: # liste boş mu kontrol ediyoruz
    print("kullanıcı bulmamız lazım laa hadi bir şeyler yap")
else:
    print("sıkıntı yok kullanıcı var ekmek var su var ev var iş var")        
"""     
################################################################
# LİSTEYİ KOPYALAYIP LİSTELERİ KARŞILAŞTIRARAK ŞARTA GÖRE İŞLEM YAPMAK
# KULLANNICI ADI KONTROLÜ    
"""
current_users = ["SEMİH","dilara","asude","Batu","emine"]    
new_users = ["ayşe","semih","batu","nisa","hüseyin","asude","emine"]
    
kopya = current_users[:]


for user in new_users :
    if user in kopya :
        print("üzgünüz bu isimde bir kullanıcı mevcut lütfen başka bir isim tercih ediniz.")
    else :
        print("Bu kullanıcı adını kullanabilirsiniz")        
"""    
################################################################
# SIRA NUMARALARIYLA İLGİLİ İFADELERİN YAZILMASI
"""    
sayı = [1,2,3,4,5,6,7,8,9]

for sıra in sayı :
    if sıra == 1 :
        print("1st")
    elif sıra == 2 :
        print("2nd")
    elif sıra == 3 :
        print("3rd")
    else :
        print(f"{sıra}th")                
"""        
################################################################    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    