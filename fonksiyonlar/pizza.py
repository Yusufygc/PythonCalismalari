def pizzaYap(boyut,eklenecek_malzemeler): # burda aslında *eklenecek_malzemeler bu şekil kullanıyordum ama kod yazarken değiştirdim

    print(f"Seçilen boyut : {boyut} . pizzanız hazırlanıyor.\n")

    print("malzemeler ekleniyorrr : ")

    for i in eklenecek_malzemeler:
        print("*\t\t",i)
    return