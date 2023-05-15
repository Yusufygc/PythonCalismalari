################################# SÖZLÜKLER ####################################
"""
alien0 = {"renk":"yeşil","puan":5}
print(alien0["renk"])
print(alien0["puan"])

new_points = alien0["puan"]
print(f"{new_points} puan kazandınız")

alien0["x_position"] = 0  # yeni anahtar-değer eklemek
alien0["y_position"] = 25
print(alien0)
"""
########################################################################
"""
alien1 ={}

alien1["renk"] = "mor"  # yeni anahtar-değer eklemek
alien1["puan"] = 15

print(alien1)
"""
########################################################################
"""
alien2 ={"renk": "mavi"}
print(f"uzaylı {alien2['renk']} renktedir.")

alien2["renk"] = "sarı"
print(f"uzaylı şimdi {alien2['renk']} renktedir. ")
"""
########################################################################
"""
alien = {"x_position": 0, "y_position": 25 ,"hız": "yavaş"}
print(f"original x-konumu : {alien['x_position']}")

#alien["hız"] = "hızlı   BÖLE YAPARSAK EĞER DEĞİŞTİRİP ARTIRMIŞ OLURUZ.

# uzaylıyı sağa hareket ettir
# mevcut hızına bağlı olarak uzaylının 
# ne kadar hareket ettirileceğini belirle 

if alien["hız"]== "yavaş":
    x_increment = 1
elif alien["hız"]== "orta":
    x_increment = 2
else:
    #bu şerro hızlı galiba
    x_increment = 3

# yeni konum , eski konum  artımıdır (increment)

alien["x_position"] = alien["x_position"] + x_increment
print(f"Yeni x-konumu : {alien['x_position']}")
"""
########################################################################
"""
alien0 = {"renk":"yeşil","puan":5}

del alien0["renk"]
del alien0["puan"]
print(alien0)
""" 
########################################################################
"""
# PARANTEZ İÇİNİ SIRALI KULLANMAK VE BENZER NESNELERİN SIRALANMASI
favori_languages ={
    "ayşe": "python",
    "ahmet": "java",
    "dilara": "c",
    "soner": "swift",
}

language = favori_languages["ahmet"].title()


print(f"{language} ahmet'in favori dilidir.")
print(favori_languages)
"""
########################################################################
"""
# DEĞERLERE ERİŞMEK İÇİN get() KULLANMAK
#GET EĞER ANAHTARIN DEĞERİ YOKSA HATA YERİNE BİZİM VERDİĞİMİZ VARSAYILAN 
#DEĞERİ GÖSTERİR EĞER BİZ DEĞER VERMEZSEK YİNE HATA YERİNE "NONE" DEĞERİ
#YANİ HİÇBİR DEĞERİ YOK YAZDIRIR.

# USING get() TO REACH VALUE
# IF KEY HASN'T GOT A VALUE ,get() SHOWS US THAT WE GIVE A ALTERNATIF VALUE
#INSTEAD OF FAİL. IF WE DON'T GİVE A VALUE , get() SHOWS US NONE WHIC MEANS
#IT HAS NO VALUE. INSTEAD OF FAİL


alien0 = {"renk":"yeşil","puan":5}

point_value = alien0.get("puan","hiçbir puan değeri atanmamış")
print(point_value)

point_value = alien0.get("tür","hiçbir tür değeri atanmamış")
print(point_value)

# EĞER PUANIN DEĞERİ VARSA YAZDIRIR.
# IF PUAN HAS A VALUE,PUAN IS WRITTEN.

# KÖŞELİ PARANTEZ KULLANMAKTAN DAHA FAYDALI 
# USING get() IS MORE USEFUL THAN box brackets 
"""
########################################################################
"""
person = {
    "first_name": "EYÜP",
    "second _name": "YAĞCI",
    "city": "Kayseri",
    "age" : 46
}
print(person)
"""
"""
friends_lucky_numbers = {
    "ayşe": 26,
    "semih": 42,
    "emine": 38,
    "erva": 54,
    "asude": 10,
    "batu" : 34,
}

print(friends_lucky_numbers)

for key , value in friends_lucky_numbers.items():
    print(f"\nisim : {key}")
    print(f"şanslı sayı : {value}")
"""
"""

learned_words = {
    "if " : "conditional",
    "print ": "write",
    "for ": "loop",
    "list ": "ordinal values",
    "dimension " : "unchangeable list",
}

for key, value in learned_words.items():
    print(f"\nenaktar:{key}")
    print(f"değer : {value}")
"""
########################################################################
""" 
# USING FOR LOOP TO REACH KEY AND VALUE 
 
user = {
    "username": "yusufi",
    "firs_n": "yusuf",
    "second_n":"yağcı",
}

for key , value in user.items():
    print(f"\nanahtar:{key}")
    print(f"değer:{value}")
"""    
########################################################################
"""
# ANAHTARLAR ÜZERİNDEN DÖNGÜ KURMAK 

favori_languages ={
    "ayşe": "python",
    "ahmet": "java",
    "dilara": "c",
    "soner": "swift",
}

for name in favori_languages.keys():
    print(name.title())

# AYNI SONUCU VERDİ BU YÜZDEN .keys() NASIL İŞİMİZE GELECEKSE ÖYLE KULLANABİLİRİZ

for name in favori_languages:
    print(name.title())

""" 
########################################################################
"""
favori ={
    "ayşe": "python",
    "ahmet": "java",
    "dilara": "c",
    "soner": "swift",
}

friends = ["ayşe","ahmet"]

for name in favori.keys():
    print(f"'merhaba, {name.title()}.'")
    language = favori[name].title()
    print(f"{name} 'ın en sevdiği dil : ", language)

    if name in friends:
        #language = favori[name].title()
        print(f"\n{name.title()}, {language} dilini sevdiğini görüyorum!")

if 'mehmet' not in favori.keys():
    print("mehmet lütfen anketimize katıl !")
 
"""
########################################################################
"""  
#print(kanks[isim]) -----> bu şehirleri nasıl yazdırıyor ?  

kanks = {
    "ogi":"konya",
    "ahmet": "istanbul",
    "mırat": "kastamonu",
    "omar": "malatya",
    "bekzod": "özbekistan",
}

for isim in kanks.keys():
    # print(isim)
    # print(f"selamün aleyküm {isim.upper()}")
    print(kanks[isim])
     """
########################################################################
"""
# SIRALI BİR ŞEKİLDE YAZDIRMAYI SAĞLAR
favori_languages ={
    "ayşe": "python",
    "ahmet": "java",
    "dilara": "c",
    "soner": "swift",
}

for name in sorted(favori_languages.keys()):
    print(f"{name.title()} , ankete katıldığın için teşekkürler.") 

for dil in sorted(favori_languages.values()):
    print(dil)
"""    
########################################################################
"""
# DEĞERLER ÜZERİNDEN DÖNGÜ KURMAK

favori_languages ={
    "ayşe": "python",
    "ahmet": "java",
    "dilara": "c",
    "soner": "swift",
}

print("aşağıdaki diller tercih edilmiştir :")
for languages in sorted(favori_languages.values()):
    print(languages.title())
"""
########################################################################
"""
# DEĞERLERİN İÇİNDE TEKRAR EDEN VERİLER OLABİLİR O YÜZDEN KÜME ŞEKLİNDE
#ÇEKEBLİRİZ

favori_languages ={
    "ayşe": "python",
    "ahmet": "java",
    "dilara": "c",
    "soner": "swift",
    "elif": "python",
    "hüso": "java",
    "alp": "c++"
}

for languages in set(favori_languages.values()):
    print(languages.title())

# KÜMELER

diller = {"python","python","c++","java","java","c#","c++"}
print(diller)

# küme same dictionary but küme hasn't got a key-value . it has just a data
# so you can understand what are you looking and kümes don't exist a ordinal
# value in comparison with list and dictionary.
""" 
########################################################################
""" # ETKİNLİK 
learned_words = {
    "if " : "conditional",
    "print ": "write",
    "for ": "loop",
    "list ": "ordinal values",
    "dimension " : "unchangeable list",
    "vsc": "platform",
    "python": " language",
    "fonksiyon":"kullanışlı",
    "class" : "sınıflar",
    "DPL" : "amazing area"
}
for key , value in learned_words.items():
    print(f"\nyazılım sözlüğü : {key}")
    print(f"anlamı : {value}")
 


example= {
    "mısır": "nil",
    "bulgaristan": "tuna",
    "suriye": "fırat",
}

for ülke , nehir in example.items():
    print(f"{nehir} nehri {ülke}'nin içinden akar ")


for nehir in example.values():
    print(nehir)


for ülke in example.keys():
    print(ülke)


favori_languages ={
    "ayşe": "python",
    "ahmet": "java",
    "dilara": "c",
    "soner": "swift",
    "elif": "python",
    "hüso": "java",
    "alp": "c++"
}

persons = ["ayşe","ahmet","veli","ekrem","hüso","alperen","soner","hamza"]

for kişiler in favori_languages.keys():
    if kişiler in persons:
        print("anketi yanıtladığınız için teşekkür ederiz")
    else:
        print("lütfen anketimizi yanıtlayınız.")    
 """
########################################################################
"""
# İÇ İÇE YERLEŞTİRME 

alien1 = {"renk" : "mavi", "puan": 5}

alien2 = {"renk" : "yeşil", "puan": 10}

alien3 = {"renk" : "sarı", "puan": 15}

aliens = [alien1,alien2,alien3]

for i in aliens:
    print(i)
"""

######### NEW EXAPMLE #########
"""
# create an empty list to store aliens
aliens = []
 
# create 30 green aliens

for alien_number in range(30):
    new_alien = {"renk": "yeşil","puan": 5, "hız":"yavaş"}
    aliens.append(new_alien)

# show first 5 aliens
for alien in aliens[:5]:
    print(alien)
    print("...")
    
# show how many aliens were created.

print(f"toplam uzaylı sayısı : {len(aliens)}")
"""
 
###############
"""
magalar = []

for magam in range(12):
    old_magam = {"memleket": "kayserü", "yaş":23, "lise":"NMBAL"}
    magalar.append(old_magam)
    
    
for maga in magalar[:7]:
    print(maga)
    print("------")
    
print(f" toplam maga sayısı: {len(magalar)}")    
"""
################
"""
magalar = []

for magam in range(12):
    old_magam = {"memleket": "kayseri", "yaş":23, "lise":"NMBAL"}
    magalar.append(old_magam)

for maga in magalar[:2]:
    if maga["memleket"] == "kayseri":
        maga["yaş"] = 33
        maga["memleket"] = "talas"
        maga["lise"]= "küçükçalık"
for maga in magalar[2:5]:
    if maga["memleket"] == "kayseri":
        maga["yaş"] = "geçmiş iş bitmemiş"
        maga["memleket"] = "asarcık"
        maga["lise"]= "amet eren" 
                
for maga in magalar[:7]:
    print(maga)
    print("- - - - - -")     

"""
########################################################################
"""
 # SÖZLÜK İÇİNDE LİSTE 

pizza = {
    "hamur": "kalın",
    "malzemeler" : ["mantar","peperonni","fazladan peynir"]
}

print(f"aşağıdaki malzemlerle birlikte {pizza['hamur']}"
      "-hamurlu pizza siparişi verdiniz :")

for topping in pizza["malzemeler"]:
    print(f"\t{topping}")
 
"""
###############################

"""
favori_languages ={
    "ayşe": ["python","c"],
    "ahmet": ["js","java"],
    "dilara": "c",
    "soner": ["swift","kotlin"],
   
}

for name , languages in favori_languages.items():
    print(f"\n{name.title()}'in favori dilleri :")
    for language in languages:
        print(f"\t{language.title()}")
"""


########################################################################
"""
sözlük = {
    "name": "yusuf",
    "last_name":"yagci",
    "number" : 456
} 

sözlük1 = {
    "name":"cafer",
    "last_name": "delitayfunoğulları",
    "number": 345
}

people = [sözlük,sözlük1]

for insan in people:
    print(insan) 
""" 
##################333
""" 
hayvan = {
    "tür": "köpek",
    "sahip adı": "ismail",
}

hayvan1 = {
    "tür": "kedi",
    "sahip adı": "remzi",
}

hayvan2 = {
    "tür": "balık",
    "sahip adı": "haydar",
}

pets = [hayvan,hayvan1,hayvan2]

for a in pets:
    print(a) 
"""
###########################
"""
favourite_places ={
    "nalan": [" istanbul","ankara","izmir"],
    "emircan":["kayseri","manisa","sakarya"],
    "buray": ["danimarka", "estonya","çekya"],
}

for name , places in favourite_places.items():
    for place in places:
            print(f"\n{name}'in favori mekanları : {place}")
"""   
########################################################################
"""
kişiler ={
    "ali": [1,2,3,4],
    "cafer": [12,34,35],
    "ismail": [78,89,90],
}

for isim, sayı in kişiler.items():
    print(f"kişi : {isim}")
    print(f"en seviği sayılar: {sayı}") 
"""
########################################
"""
cities= {
    "sakarya":{
        "country":"türkiye",
        "popülation": "1M",
        "fact": "minimal",
    },
    "new york":{
        "country":"USA",
        "popülation" :"35M",
        "fact": "city of money",
    },
    "londra":{
        "country":"england",
        "popülation": "20M",
        "fact": "city of rain",
    },
}
"""

#for şehir , özellikleri in cities.items():
#    print(f"""{şehir}:
#        country: {özellikleri["country"]},
#        popülation : {özellikleri["popülation"]},
#        information : {özellikleri["fact"]}. 
        
#    """)

########################################