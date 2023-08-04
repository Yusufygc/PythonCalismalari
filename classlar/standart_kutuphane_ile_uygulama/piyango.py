
from random import choice

bilet_elemanlari = [1,2,3,4,5,6,7,8,9,10,"a","b","c","d","e"]

def bilet_olustur():
    bilet = []
    while len(bilet) < 6:
        eleman = choice(bilet_elemanlari)
        if eleman not in bilet:
            bilet.append(eleman)
    return bilet

ödül_bileti = bilet_olustur()
bireysel_bilet = bilet_olustur()

if bireysel_bilet == ödül_bileti:
    print("Tebrikler, 1000 TL kazandınız!")
else:
    print("\nMaalesef, bileti tutturamadınız.")
    print("Bileti tutturan numaralar: ")
    print(ödül_bileti)
    print("Biletiniz: ")
    print(bireysel_bilet)
    print("Daha sonra tekrar deneyiniz iyi günler.")

#####################
# piyango analizi

my_ticket = [1,5,6,4,"a","b"]
count = 0
while True:
    ödül_bileti2 = bilet_olustur()
    count += 1
    if my_ticket == ödül_bileti2:
        print("Tebrikler, {} denemede bileti tutturdunuz.".format(count))
        break
