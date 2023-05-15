
############################ CONDITIONAL STATEMENTS ################
"""
cars =["audi","bmw","togg","bentley"]

for i in cars:
    if i == "bmw":         # "=" bu eşitlerken "==" bu, değeri kontrol eder 
        print(i.upper())
    else:
        print(i.title())    
"""
##########################################################
"""
# != ---> eşitsizzliği kontrol eder.

istek = "mantar"
if istek != "ançüez":
    print("ançüez istemezüm ha !!")
"""
##########################################################
"""
A=str(input("isminiz :"))

names = ["ali","veli","cafer"]

if A in names:
    print(f"hoşgeldin {A} kardeş")
else :
    print("daha gelmedi paşa hazretleri")
"""
############################################################
"""
#akraba = ["teyze","dayii""dede","hacıanne","amca"]

banlanmış_persons = ["remzi","burak","berke","nalan","fadime"]

user = "abdülhey"

if user not in banlanmış_persons:
    print(f"Sayın {user.upper()} , yorumunuzu yazabilirsiniz.")
"""
############################################################
"""
vote = int(input("lütfen yaşınızı giriniz :"))

if vote <= 18 :
    print("oy moy veremezssiniz büyüyüp de gelin")
else:
    print("oy namustur kime verdiğine niye verdiğine ayık ol.Allah'a emanet.")    
"""
############################################################
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
############################################################
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
############################################################
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
############################################################  
"""
istek_listesi = ["mantar","yeşil biber","fazladan peynir"]

for istekler in istek_listesi:
    if istekler == "yeşil biber":
        print("gusura galma elimizde büber yok")
    else:    
        print(f"{istekler} ekleniyor")
    
print("\nPiZZanız hazarlanıyür")    
"""
############################################################  
"""
istek_listesi = []

if istek_listesi:
    for istekler in istek_listesi:
        print(f"{istekler} ekleniyor")     
    print("pizzanız haziirr")
else:
    print("Düz pizza istediğinizden emin misiniz? ")    
"""
############################################################
"""
var_olanlar = ["mantar","zeytin","yeşil biber","pepperoni","ananas","fazla peynir"]
istenilen = ["mantar","patates kızartması","fazla peynir"]    
    
for istek in istenilen :
    if istek in var_olanlar :
        print(f"{istek} ekleniyor.")
    else :
        print(f"sorry ,{istek} yok.")
print("\nPizzanız hazır!")                
"""    
############################################################ 
"""    
names = ["admin","musti","ilayda","semih","ayşe"]    
    
for user in names :
    if user =='admin':
        print("selamünaleyküm amdin,durum raporunu görmek ister misin?")
    else :
        print(f"merhaba {user}, tekrar oturum açtığın için teşekkürler.")        
    
    
if names == []:
    print("kullanıcı bulmamız lazım laa hadi bir şeyler yap")
else:
    print("sıkıntı yok kullanıcı var ekmek var GOO")        
"""     
############################################################    
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
############################################################
"""    
sayı = [1,2,3,4,5,6,7,8,9]

for vaov in sayı :
    if vaov == 1 :
        print("1st")
    elif vaov == 2 :
        print("2nd")
    elif vaov == 3 :
        print("3rd")
    else :
        print(f"{vaov}th")                
"""        
############################################################    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    