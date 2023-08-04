#print(38/0) # AŞAĞIDAKİ MESAJI ALIRIZ.

# Traceback (most recent call last):
#   File "c:\Users\TUF Dash F15\Desktop\python_kitabi_calismalari\Dosya_islemleri_ve_ozel_durumlar\ozel_durumlar\zeroDivision.py", line 1, in <module>
#     print(38/0)
# ZeroDivisionError: division by zero

# ÖZEL DURUMLARDA HATA MESAJI YAZDIRMAK // TRY-EXCEPT \\ BLOKLARI İLE MÜMKÜNDÜR.

try:
    print(38/0)
except ZeroDivisionError:
    print("Bir sayıyı 0'a bölemezsiniz.")

# ÇÖKMELERİ ENGELLEMEK İÇİN TRY-EXCEPT BLOKLARI VE ÖZEL DURUMLAR KULLANILIR.

print("ikis sayıyı bölmek için 2 sayı giriniz.")
print("Çıkmak için 'q' tuşuna basınız.")
while True:
    a = input("Birinci sayı: ")
    if a == 'q':
        break
    b = input("İkinci sayı: ")
    if b == 'q':
        break
    try:
        sonuc = int(a) / int(b)
    except ZeroDivisionError:
        print("Bir sayıyı 0'a bölemezsiniz.")
    else:
        print(sonuc)


