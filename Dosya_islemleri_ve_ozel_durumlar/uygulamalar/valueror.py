while True:
    try:
        sayi1= int(input("Birinci sayıyı giriniz: "))
        sayi2= int(input("İkinci sayıyı giriniz: "))
        toplam = sayi1 + sayi2
    
    except ValueError:
        print("Lütfen sayı giriniz.geçersiz değer girdiniz")
    else:
        print("Toplam: ", toplam)
        break