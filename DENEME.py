import fonksiyonlar.pizza as pizza

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
                #break

            else:
                print("yanlış işlem lütfen tekrar deneyiniz.\n")
            
            break

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
        break            

yemek = pizza.pizzaYap(size,malzemeler)

print(yemek)