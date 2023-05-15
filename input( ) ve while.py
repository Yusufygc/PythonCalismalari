############################### INPUT (KULLANICI GİRDİSİ) ######################
"""
promt = "bana kim olduğunu söylersen sana kim olduğunu söylerim."
promt += "\nsen kimsin la "

name = input(promt)
print(f"\nmerhaBAAAA ,{name}")

"""
##############################################################

# SAYISAL GİRDİLER İÇİN İNT KULLANMAK . PYTHON GİRDİYİ STRİNG BİR İFADE OLARAK 
# DÖNDÜRÜR SAYI GİRSEK BİLE . YAZDIRIRKEN TIRNAK İÇİNDE YAZDIRIR . AMA KARŞILAŞTIRMA
# TARZI UYGULAMALARDA HATA VERİR ÇÜNKÜ STRİNG İLE İNT OR FLOAT DEĞER KARŞILAŞTIRILAMAZ
"""
age = input("kaç yaşınızdasınız :")
print(age)

if age > 18:
    print("18 den büyük")

# if age > 18:
# TypeError: '>' not supported between instances of 'str' and 
# 'int'
"""
"""
age = int(input("kaç yaşınızdasınız :"))
print(age)

if age > 18:
    print("18 den büyük")
"""
##############################################################
"""
boy =int(input("Lütfen boyunuzu belirtiniz :"))
cinsiyet = input("lütfen cinsiyetinizi belirtiniz :")

if 155 < boy < 180 and cinsiyet =="erkek":
    print("asker olmak için kriterleriniz uygundur")
    
elif 180 < boy < 190 and cinsiyet =="erkek":
    print("pilot olmak için kriterleriniz uygundur")

elif boy > 190 and cinsiyet =="erkek":
    print("sırma boylu yağız delikanlısın ama pilot olamazsın")    

else:
    print("asker olmak için kriterleriniz uygun değildir.")
"""
##############################################################
"""
sayı = int(input("bir sayı gireceksin onun gibi bırakıp gitmeyecek... :"))

if sayı % 2 == 0:
    print("bu sayı çifttir")
    sayı2 = input("başka bir sayı girmek ister misin :")
    if sayı2 == "evet":
        new = int(input("you can write a number again :"))
        if new % 2 != 0:
            print("bu sefer tek sayı girdiniz")
    elif sayı2 == "hayır":
        print("peki öyle olsun allah'a emanet ol hayırlı günler.")
elif sayı % 2 != 0:
    print("bu sayı tektir.")       
"""   
##############################################################
"""
# RENT A CAR EXAMPLE

araç = input("hangi marka arabara kiralamak istersiniz :")

var_olanlar = ["audi","bwm","hyundai","nissan","egea","volkswagen","toyota","ford","kia","jeep","mini cooper"]
lüks =["rolls royce","ferrari","lamborghini","bentley","aston martin","mcLaren",]

if araç in var_olanlar:
    print("tercihiniz için teşekkür eder aracınızı en kısa zamanda hazırlayacağımıza emin olabilirsiniz. ")
elif araç in lüks:
    print("bunu kim kaybetmişte biz kiralayalım güzel kardeşim! ")
else:
    print("istediğiniz marka bir aracımız bulunmamaktadır")
    b=input("elimizde olan araçları görmek ister misiniz :")
    if b == "evet":
        print("hemen gösteriyorum :")
        for i in var_olanlar:
            print(i)
    else:
        print("peki teşekkür eder iyi günler dileriz.")    
"""
##############################################################   
"""
rezerve =int(input("akşam yemeği programı için kaç kişi geleceksiniz :"))

if rezerve > 8 and rezerve % 2 == 0 :
    print("daha büyük bir masayı hazırlamamız için beklemeniz gerekmetedir")
elif rezerve > 8 and rezerve % 2 != 0 :
    print("ekstra masa birleştirmemiz gerekebilir bu yüzden ücretlendirme değişebilir")
    c = input("yine de devam etmek ister misiniz ? :")
    if c == "evet":
        print("tamamdır masanızı en kısa sürede hazırlayacağız.")
    else:
        print("peki.iyi günler dileriz")
pass
"""
##############################################################
"""
kat = int(input("lütfen bir sayı giriniz :"))

if kat % 10 == 0:
    print("bu sayı 10'un katıdır.")
else:
    print("hımmm güzel sayı neden bunu seçtin ??? neyse haberin olsun 10'un katı değil")
"""
##############################################################

                ################ WHİLE ###############
"""
ilk_sayı = 2

while ilk_sayı <= 6:
    print(ilk_sayı)
    ilk_sayı += 1
"""    
############################################################
"""
h = "\nBana bir şey söyle sana onu tekrar edeyim :"
h +="\nprogramı sonlandırmak için 'quit' giriniz . "

message =""
while message != 'quit':
    message= input(h)
    if message != 'quit': # quiti tekrar yazdırmasını önlemiş oluruz bu şekilde.programdan direkt çıkar.
        print(message)
"""
############################################################
""" #  ######## bayrak kullanmak

oyun = " \ngitmek istediğniz yönü yazınız(sadece sağ veya sol) "
oyun += " \nçıkmak isterseniz quit yazınız :"

active =True
while active:
    mesaj = input(oyun)
    if mesaj == 'quit':
        active = False
    else:
        print(f"{mesaj} taraftan gidilecektir.")    

"""
############################################################
""" ###################### break kullanmak
şehir = "\nLütfen gitmek istediğiniz şehrin adını giriniz"
şehir +="\neğer bedava olduğu halde bu kampanyadan faydalanmak istemiyorsanız q yazınız :"

while True:
    gezi = input(şehir)
    
    if gezi == 'q':
        break
    else:
        print(f"{gezi.title()} şehrine gidiş için biletiniz ayarlanıyor.")
"""
############################################################

###### continue = geri kalan kodu çalıştırmadan döngüden tamamen çıkmak yerine koşullu
###### bir testin sonucuna bağlı olarak " DÖNGÜNÜN BAŞINA DÖNMEK İÇİN KULLANILIR ".
"""
ilk_sayı = 0

while ilk_sayı < 10 :
    ilk_sayı += 1
    if ilk_sayı % 2 == 0 :
        continue
    print(ilk_sayı)
"""        

"""
sayı = 0

while sayı <= 20:
    sayı += 1
    if sayı % 2 != 0 :
        continue
    print(sayı**2)
"""
############################################################

# eğer ki programı sonsuz döngüye sokarsan ctrl + c ile ya da direkt terminali kaptarak kurtulabilirsin

############################################################
"""
malzeme = "istediğiniz malzemeyi yazınız. "
malzeme += "tercihlerinizi q ya basarak sonlandırabilirsiniz. :"

malzemeList =[]

while True:
    istek = input(malzeme)
    if istek == "q":
        break
    print(f"{istek} pizzanıza eklenecektir.")
    malzemeList.append(istek)

print("seçtiğiniz malzemeler şunlardır :")

for i in malzemeList:
    print(i)
    #devam = input("eklemek istediğiniz başka malzeme varmı ?")
    #if devam == "evet":
    # vatnadaş eklemeyi unuttuğu malzemeyi eklemek için tekrardan while nasıl sokarım
"""       
############################################################
"""
while True:
    
    yaş =int(input("ücretlendirme için yaşınızı giriniz :"))
    # BAK GÜZEL KARDEŞİM PYTHON İNPUT DEĞERLERİNİ NORMALDE STRİNG ALIR O YÜZDEN İNT'E ÇEVİRMEYİ UNUTMA
    if yaş < 3:
        print("girişiniz ücretsizdir")
    
    elif 3 < yaş < 12:
        print("ücretiniz 10 tl'dir.")
    else:
        print("ücretiniz 20 tl'dir.")
        break
"""        
############################################################
"""
# etkinlik---> döngünün ne kadar uzun çalışacağını kontrol etmek için activi kullanmak.

active = True
while active:
    
    yaş =int(input("ücretlendirme için yaşınızı giriniz :"))
    # BAK GÜZEL KARDEŞİM PYTHON İNPUT DEĞERLERİNİ NORMALDE STRİNG ALIR O YÜZDEN İNT'E ÇEVİRMEYİ UNUTMA
    if yaş < 3:
        print("girişiniz ücretsizdir")
    
    elif 3 < yaş < 12:
        print("ücretiniz 10 tl'dir.")
    else:
        print("ücretiniz 20 tl'dir.")
        active = False
"""
############################################################
"""
##########  BİR LİSTENİN ELEMANLARINI BAŞKA BİR LİSTEYE TAŞIMA #######
 
# doğrulanması gereken kullanıcılarla ve onaylanmış kullanıcıları tutmak için boş bir listeyle
# başla.

onaylanmamış_kullanıcılar = ["tesniye","şükriye","serdar"]
onaylanmış_kullanıcılar = []

# onaylanmamış kullanıcı kalmayana kadar her kullanıcıyı doğrula.
# doğrulanmış her kullanıcıyı onaylanmış kullanıcılar listesine taşı.

while onaylanmamış_kullanıcılar:
    mevcut_kullanıcı = onaylanmamış_kullanıcılar.pop()
    # onaylanmamış kullanıcılar listesi boşalana kadar while döngüsü devam eder boşalınca durur.
    print(f"kullanıcı doğrulanıyor : {mevcut_kullanıcı.title()} ")
    onaylanmış_kullanıcılar.append(mevcut_kullanıcı)
    
    # bütün onaylanmış kullanıcıları görüntüle
print("\nAşağıdaki kullanıcılar onaylanmıştır :")
for kullanıcı in onaylanmış_kullanıcılar:
    print(kullanıcı.title())    

# print(onaylanmamış_kullanıcılar)
# print(onaylanmış_kullanıcılar)
"""
############################################################
"""
eşşek_olanlar = ["çalışmayanlar","zaman israfı yapanlar","kararsız olanlar"]
akıllananlar = []

while eşşek_olanlar:
    uslanmaya_başlayanlar =eşşek_olanlar.pop()
    akıllananlar.append(uslanmaya_başlayanlar)
    print(f"terbiye ediliyor : {uslanmaya_başlayanlar}")
print("\nterbiye işlemi başarı ile gerçekleştirilmiştir.bunlar artık terrrrrbiyyyeli tavuk")

for i in akıllananlar:
    print(f"terbiye edilenler :{i}")    
"""
############################################################
"""
##### LİSTEDEN TEKRAR EDEN ELEMANLARI SİLMEK ##########
# while çalışmaya başlar ve listedeki kediyle ilk karşılaşmasında onu siler sonra
# tekrar listeye girer bir de ne görsün bir tane daha kedi var onuda siler
# sonra tekrar listeye girer ve bir tane daha kedi görünce derki la havla vala guvvetee illa billah yauğv
# ve onu da siler sonra tekrar listeye girer bir yoklar etrafı kedi var mı diye 
# baktı ki kedi yok kod sırasını salar (bu tekrar eden bütün değerler için geçerlidir.)
 
evcil_hayvanlar = ["kedi","köpek","kuş","kedi","balık","yılan","kedi"]

print(evcil_hayvanlar)

while "kedi" in evcil_hayvanlar:
    evcil_hayvanlar.remove("kedi")

print(evcil_hayvanlar)    
"""
##############################################################
"""
cars = ["bmw","togg","mercedes","tesla","dodge","ford","bmw","ford","togg","mercedes","mercedes"]

print(cars)

while "mercedes" and "togg" and "ford" in cars:
    cars.remove("mercedes")
    cars.remove("togg")
    cars.remove("ford")

print(cars)
"""
##############################################################
# ÜSTTE VE ALTTA BİR GARİPLİK VAR TAM ANLAMADIM ALİNİN HEPSİNİ NEDEN SİLMİYO LA
#################################################3
"""
clasroom = ["ali","ali","ali","ali","ayşe","ayşe","ayşe","fatma","fatma","fatma"]

print(clasroom)

while "ali" and "ayşe" and "fatma" in clasroom:
    clasroom.remove("ali")
    clasroom.remove("ayşe")
    clasroom.remove("fatma")

print(clasroom)
"""
##############################################################
#### İNANILMAZ LEZZETTLİ USTAAMMM ######33
"""
responses = {}

active = True

while active:
    name =input("\nisminiz nedir ? : ")
    response = input("hangi dağa tırmanmak isterdiniz ? : ")

    responses[name] = response # yanıtı sözlükte saklıyoruz

    repeat = input("Başka bir kişinin yanıtlamasını ister misiniz (evet/hayır) :")
    
    if repeat == "hayır":
        active = False

# anket tamamlandı sonuçları göster
print("\n------ Anket sonuçları ------")

for name , response in responses.items():
    print(f"{name} , {response} dağına tırmanmak istiyor.")
"""
##############################################################
"""
yemek_siparis = ["hamburger","lahmacun","pizza","kebab"]

hazırlanan_siparis = []

for i in yemek_siparis:
    print(f"{i} siparisiniz hazırlanıyor")
    
while yemek_siparis:   
    hazır = yemek_siparis.pop()
    hazırlanan_siparis.append(hazır)
     
print("\nsiparisleriniz hazırlanmıştır :")
print("\n\t------Siparis listesi------")
print(hazırlanan_siparis)
print(yemek_siparis)

"""
##############################################################
"""
yemek_siparis = ["pastırma","hamburger","lahmacun","pastırma","pizza","kebab","pastırma"]

hazırlanan_siparis = []

print("pastırma dışındaki siparişleriniz hazırlanıyor.Çünkü hiç pastırmamız kalmamış malesef.")

while yemek_siparis:   
    hazır = yemek_siparis.pop()
    hazırlanan_siparis.append(hazır)

while "pastırma" in hazırlanan_siparis:
    hazırlanan_siparis.remove("pastırma") 

for i in hazırlanan_siparis:
    print(f"{i} siparisleriniz hazırlanıyor.")    

print("\nsiparisleriniz hazırlanmıştır :")
print("\n\t------Siparis listesi------")
print(hazırlanan_siparis)
print(yemek_siparis)
"""
##############################################################
"""
tatil = {}

while True:
    name = input("lütfen isminizi giriniz : ")
    mekan =input("dünyada ziyaret edecek olsaydınız nereyi ziyaret etmek isterdiniz : ")
    tatil[name]= mekan
    tekrar = input("işleme devam etmek ister misiniz(evet/hayır) ? : ")
    if tekrar == "hayır":
        break

for isim , yer in tatil.items():
    print(f"{isim} {yer} e gitmek istiyor.")
"""
##############################################################
