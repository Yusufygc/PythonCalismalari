file ="C:\\Users\\TUF Dash F15\\Desktop\\python_kitabi_calismalari\\Dosya_islemleri_ve_ozel_durumlar\\uygulamalar\\ortak_kelimeler\\alice.txt"

try:
    with open(file , encoding='utf-8') as file_object:
        lines=file_object.readlines()
        
    alice_string = ''  

    for line in lines:
        alice_string += line.strip()
        
    alice_string = alice_string.lower()
    amount =alice_string.count(" the ")
    print(f"the kelimesi {amount} defa geçiyor.")

except FileNotFoundError:
    print("Dosya bulunamadı.")