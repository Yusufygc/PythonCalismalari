##################################################################
##                        # FUNCTION #                          ##
##################################################################

##################################################################
# FONKSIYONLAR BIR DEFA TANIMLANIR VE ISTEDIĞIMIZ KADAR ÇAĞIRABILIRIZ.
"""
def kullanıcıyı_selamla():
    # Çıtır bir selamlama 
    print("hello")
    
kullanıcıyı_selamla()    



b = input("lütfen bir isim giriniz : ")

def fitneci_avla():
    if b == "serdar":
        print("fitneci avlanmıştır")
    else:
        print("araştırılıyor ")    

fitneci_avla()
"""
####################################################################
# UYGULAMA - FONKSİYON KULLANIMI 
"""
def selam_ver(username):
    print(f" Selamün aleyküm {username.title()}")
    
selam_ver("tyler durden")    

selam_ver("patrick bateman")

"""
####################################################################
# FONKSİYONA PARAMETRE GÖNDERMEK
"""
def haber_ver():
    print("zaatı şahane fonksiyonları öğreniyor")
    
haber_ver()

def favori_kitap(username):
    print(f"{username.title()} en sevdiğim kitaplardandır.")
    
favori_kitap("monte kristo kontu")

def padişah(adı,kaçıncı):
    print(f"sultan {kaçıncı} {adı.title()} huzura teşrif etmişlerdir")

padişah("mehmet","2.")
"""
####################################################################
### BTK AKADEMİ UĞRAŞMACA ###
"""
def tekrarlat( kelime , adet):
    print(kelime * adet )

tekrarlat("baba kodluyor\n" , 5)

def calis_köle(emir , tekrar):
    print(emir * tekrar)

calis_köle("\n\todun kes", 3)
"""
#########################################
# '*' bu listeye '**' bu da sözlüğe çevirir
"""
def listeye_cevir(*args):   
    liste = []
    for arg in args:
        liste.append(arg)
        
    return liste

sonuc =listeye_cevir(12,10,115,"hii",95,"selamss")

print(sonuc)
"""
####################################################################
########## ARGÜMAN GÖNDERMEK ##########
#### KONUMSAL ARGÜMANLAR #####
"""
def describe_pet(animal_type, pet_name) :
    print(f"\n ben bir {animal_type} sahibiyim")
    print(f"\nhayvanımın adı {pet_name} dir")

describe_pet("kedi","eylül")

describe_pet("kuş","cicik")
"""
#### konumsal argümanlarda sıraya dikkat etmek gerekir . etmezsen komik veyahut rezil şeylerle karşılaşabilirsin
####################################################################
##### ANAHTAR KELIME ARGÜMANLARI ##### 
"""
def describe_pet(animal_type, pet_name) :
    print(f"\n ben bir {animal_type} sahibiyim")
    print(f"\nhayvanımın adı {pet_name} dir")

describe_pet(animal_type="kedi",pet_name="eylül")
"""
####################################################################
############ VARSAYILAN DEĞER ##########
# eğer parametreye direkt varsayılan değer verirsek ve daha sonra değiştirmezsek
# python otomatik olarak o değeri kabul eder ama istersek değiştirebiliriz.
"""
def describe_pet(pet_name,animal_type= "kedi" ) : # değer atamadığımız argüman önce gelmeli.
    print(f"\n ben bir {animal_type} sahibiyim")
    print(f"\nhayvanımın adı {pet_name} dir")


describe_pet("eylül")

describe_pet("yılan", "çıngırak") # konumsal argüman hatası yaptım DİKKATLİ OL !!!

describe_pet("çıngırak", "yılan")
"""
####################################################################
# ÇITIR UYGULAMA
"""
# 1.
def tisort(yazı,boy):
    print(f" {yazı} ")
    print(f"bu şahane tişörtün bedeni {boy} dir")


tisort(yazı= "1o numara tişört",boy =" M")

# 2.
def tisort(yazı,boy="L"):
    print(f" {yazı} ")
    print(f"bu şahane tişörtün bedeni {boy} dir")

tisort("pythonu severim")

# 3.
def sehir(il,ülke,kıta = "avrupa"):
    print(f"{ülke} {il} iline sahip {kıta} kıtasında bir ülkedir.")
    
sehir(il="hamburg",ülke="almanya")
sehir(il="kayseri",ülke="türkiye",kıta="hem avrupa hem asya")
sehir(ülke="Fransa",il="marsilya")
"""
####################################################################
########## RETURN - DÖNDÜRÜLEN DEĞERLER #########
# değer döndüren bir fonksiyonu çağırdığınızda döndürülen değerin atanabileceği bir değişkeni temin etmeniz gerekir.
"""
def describe_name(first_name,last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()    

scientist = describe_name("oktay","sinanoğlu")

print(scientist)
"""

####################################################################
####### BIR ARGÜMANI ISTEĞE BAĞLI HALE GETIRMEK
"""
def describe_name(first_name,last_name,middle_name=""):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
            full_name = f"{first_name} {last_name}"
    
    return full_name.title()    
# ikinci ismi isteğe bağlı hale getirdik

sultan =describe_name("mehmet","osmanoğlu")
print(sultan)

sultan = describe_name("fatih","mehmet",middle_name="sultan")
print(sultan)

aktör = describe_name("muhammed","şaşmaz","necati")
print(aktör)
"""
####################################################################
##### FONKSİYONLAR İLE SÖZLÜK TANIMLAMAK #######
"""
def cars(name,model):
    car = {"adı": name,"modeli":model}
    return car

Car=cars("canavar","dodge challanger")

print("istenilen arabanın özellikleri : ",Car)
"""
#####################################
# UYGULAMA - FONKSİYONLAR İLE SÖZLÜK TANIMLAMAK
"""
def to_become_a_man(first,second,third):
    man={"embrace":first,"loves":second,"fight type":third}
    return man
    
modern_man = to_become_a_man("his car","his wife","intelligence and disipline")

print("\n######### What shoulde be modern man's mentality #########")

print(modern_man)
"""
####################################################################
# :)
"""
def ne_olcak_bu_isler():
    print("düzelcez be abi")


ne_olcak_bu_isler()
"""
############################################################
## WHİLE DÖNGÜSÜ İLE KULLANICIDAN FONKSİYON ARGÜMANLARI İSTEMEK
"""
def person(first_name, second_name):
    ful_name = f"{first_name} {second_name}"
    return ful_name.title()

while 1: # sonsuz döngü
    print ( "\nLütfen adınızı giriniz : ")
    print("çıkış için q ya basınız.")

    first_name = input("adınız : ")
    if first_name == "q":
        print("çıkış gerçekleştirilmiştir.")
        break
    
    second_name = input("soyadınız : ")
    if second_name == "q":
        print("çıkış gerçekleştirilmiştir.")
        break

    person_name= person(first_name,second_name)
    print(f"\nHello, {person_name}")
"""
############################################################
# FONKSİYON OLUŞTURMAK VE KULLANMAK - HATIRLATMA
"""
def şehir_ülke(şehir,ülke):
    print(f"{şehir.title()} ,{ülke.title()}")

şehir_ülke("istanbul","türkiye")

şehir_ülke("berlin","almanya")

şehir_ülke("milano","italya")

"""
############################################################
# UYGULAMA
"""
def albüm(sanatçı,albüm_ismi,müzik_sayısı=None):
    şarkılar = []
    
    şarkı = {"santçının adı :":sanatçı,
             "albüm ismi : ": albüm_ismi,
              "müzik sayısı : ":müzik_sayısı}
    
    şarkılar.append(şarkı)

    for müzik in şarkılar:
          print(müzik)
    for key , value in şarkı.items():
        print(f"{key} {value}") 

while 1:
    print("Çıkış için lütfen q ya basınız.")

    isim = input("lüten sanatçı adı giriniz : ")
    if isim == "q":
        break
    
    albüm_adı = input("lüten albüm adı giriniz : ")
    if albüm_adı == "q":
         break
    break


albüm(isim,albüm_adı)
"""
############################################################
#   FONKSİYONLARA LİSTE GÖNDERMEK
"""
def selam(kişi):
    for isim in insanlar:
        mesaj= f"selamün aleyküm {isim.title()}"
        print (mesaj)


insanlar = [ "ali", "veli", "yusuf"]

selam(insanlar)
"""
############################################################
# FONKSİYON İÇERİSİNDE LİSTEYİ DEĞİŞTİRMEK
"""
basılmamış_tasarımlar = ["surat","yazı","araba"]

basılmış_modeller = []

while basılmamış_tasarımlar:
    sıradaki_tasarım = basılmamış_tasarımlar.pop()

    print(f" Basılacak model : ",sıradaki_tasarım)

    basılmış_modeller.append(sıradaki_tasarım)


print(f"\n Aşağıdaki modeller basılmıştır : ")

for basılan_model in basılmış_modeller:
    print(basılan_model)
"""

# LETS DO IT WITH FUNCTION
"""
basılmış_modeller = []

basılmamış_tasarımlar = ["surat","yazı","araba"]

def model_yazdır(basılmış,basılacak):

    while basılacak:
        sıradaki_tasarım = basılacak.pop()

        print(f" Basılacak model : ",sıradaki_tasarım)

        basılmış.append(sıradaki_tasarım)

def basılan_modeli_göster(basılmış):
    print(f"\n Aşağıdaki modeller basılmıştır : ")

    for basılan_model in basılmış:
        print(basılan_model)

model_yazdır(basılmış_modeller,basılmamış_tasarımlar )

basılan_modeli_göster(basılmış_modeller)
"""
############################################################
# ARGÜMAN OLARAK LİSTE GÖNDERMEK - ÇITIR UYGULAMA
"""
mesajlar = ["gelirken 2 ekmek al","ilacını içmeyi unutma","yarın miraç kandili dedeni ara"]


def hatırlatıcı(x):
    for i in x :
        print(i)


hatırlatıcı(mesajlar)
"""
############################################################
# ÜSTTEKİ UYGULAMANIN GENİŞLETİLMİŞ HALİ
"""
mesajlar = ["gelirken 2 ekmek al","ilacını içmeyi unutma","yarın miraç kandili dedeni ara"]

yeni_msj = mesajlar[:]

giden_mesajlar = []

def mesajKontrol(a):
    for i in a :
        print(i)

    while yeni_msj:

        taşı = yeni_msj.pop()

        giden_mesajlar.append(taşı)

#mesajKontrol(yeni_msj)

print("##################################")
print("Mesajlar : ",mesajlar)
print("##################################")
print("Yeni mesajlar : ",yeni_msj)
print("##################################")
print("Giden mesajlar : ",giden_mesajlar)

"""
############################################################
# KEYFİ SAYIDA ARGÜMAN GÖNDERMEK
"""
def malzeme(*eklenecek_malzemeler):
    print("malzemeler ekleniyorrr : ")
    for i in eklenecek_malzemeler:
        print("*\t\t",i)
       
malzeme("biber")
print("\n\n")

malzeme("sucuk","pastırma","domates","biber")
"""

# KONUMSAL VE KEYFİ ARGÜMANLARI KULLANMAK
"""
def malzeme(boyut,*eklenecek_malzemeler):

    print(f"{boyut} boyutunda pizzanız hazırlanıyor")

    print("malzemeler ekleniyorrr : ")

    for i in eklenecek_malzemeler:
        print("*\t\t",i)
       
malzeme("geniş","biber")

print("\n\n")

malzeme("orta","sucuk","pastırma","domates","biber")

"""

#KEYFİ ANAHTAR - KELİME(SÖZLÜK) ARGÜMANLAR KULLANMAK
"""
def insan(ilkAd,ikinciAd,**bilgi):
   
   print("\nkullanıcını Adı ve Soyadı : ",ilkAd +" "+ ikinciAd)
   print("\nkullanıcı hakkında bazı bilgiler : \n")

   for key ,value in bilgi.items():
        print(f"\n\t\t{key} = {value}")
   
   
kullanıcı_hakkında = insan("yusuf","yağcı",memleket = "kayseri",boy = "188 cm", kilo = "85 kg" , eğitim = "lisans" , meslek ="Bilgisayar Mühendisliği")

print(kullanıcı_hakkında) # çalıştırınca en sonda none yazıyor anlamadım onu 
"""
############################################################
# FONKSİYONLARI MODÜL HALİNE GETİRMEK --- MODÜLLER
# hayır seçeneğini seçtikten sonra direkt çıkmıyor kullanıcıdan bir daha seçim yapmasını istiyor.onu çözemedim
# her şeye evet diyince sorunsuz çalışıyor tıpkı insanlar gibi :D
"""
import pizza

size =input("Pizzanızın boyutunu giriniz : ")

print("malzeme isteğini sonlandırmak için x' e basınız.\n")

malzemeler = []

while len(malzemeler) <= 7: 
   
    malzeme =input("İstediğiniz malzemeler : ") 

    if malzeme == "x":
        break

    malzemeler.append(malzeme)

    if len(malzemeler) == 4:
        print("ücretsiz malzeme sınırına ulaştınız.Bundan soraki seçimleriniz ücrete tabidir.Her bir malzeme 10 tl\n")

        while 1:
            onay = input("Eğer onaylıyorsanız lütfen e'ye basınız.Onaylamıyorsanız h'ye basınız.")

            if onay == "e":
                print("işleminiz onaylandı seçmeye devam edebilirsiniz.\n")

                print("maksimum malzeme sınırı 7'dir.Lütfen seçimlerinizi buna göre yapınız.\n")

                if malzeme == "x":
                    break
                
                break

            elif onay == "h":
                print("pizzanız seçtiniğiniz malzemelerle hazırlanıyor.Afiyet olsun.\n")
                break

            else:
                print("yanlış işlem lütfen tekrar deneyiniz.\n")
        #break

    elif 4 <  len(malzemeler) <= 7:

        if malzeme == "x":
            break
       
        if len(malzemeler)==7:
            print("Maksimum malzeme sınırınıa ulaşıldı.\n")

            change = input("değiştirmek istediğiniz malzeme var mı(e/h) ? : ")

            while 1:
                if change == "e":
                    değiştirilecek_malzeme = input("değiştirmek istediğiniz melzeme nedir : ")

                    eklenecek_malzeme = input("eklemek istediğiniz malzeme nedir : ")

                    if değiştirilecek_malzeme in malzemeler:

                        malzemeler.remove(değiştirilecek_malzeme)

                        malzemeler.append(eklenecek_malzeme)

                        print("malzemeler değiştirilmiştir.\n")
                        break

                    else:
                        print("listenizde böyle bir malzeme yoktur lütfen tekrar deneyiniz.\n")
                        

                elif change == "h":
                    print("pizzanız seçtiniğiniz malzemelerle hazırlanıyor.Afiyet olsun.\n")
                    break
                
                else:
                    print("geçersiz işlem.tekrar deneyin")
            break
            

yemek = pizza.pizzaYap(size,malzemeler)

print(yemek)
"""