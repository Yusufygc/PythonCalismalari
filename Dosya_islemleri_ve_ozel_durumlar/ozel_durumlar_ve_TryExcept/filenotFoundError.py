file="ozel_durumlar_ve_TryExcept\\alice.txt"


try:
   with open(file,encoding='utf-8') as f:
    content=f.read()
except FileNotFoundError:
    print(f"{file} dosyası bulunamadı.")
else:
    words=content.split()
    num_words=len(words)
    print(f"{file} dosyasında yaklaşık {num_words} kelime var.")

"""
üstteki kodda FileNotFoundError hatası oluştuğunda programın çökmesini engellemek için try-except bloğu kullanıldı.
ancak except bloğunda illaki bir şey yazmak zorunda değiliz.sessizce geçmesini istiyorsak pass yazabiliriz.
ve hiçbirşey olmamış gibi yolumuza devam ederiz.

"""