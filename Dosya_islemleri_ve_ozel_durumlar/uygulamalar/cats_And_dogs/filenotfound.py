file = 'C:\\Users\\TUF Dash F15\\Desktop\\python_kitabi_calismalari\\Dosya_islemleri_ve_ozel_durumlar\\uygulamalar\\cats_And_dogs\\cats.txt'
file2 = 'C:\\Users\\TUF Dash F15\\Desktop\\python_kitabi_calismalari\\Dosya_islemleri_ve_ozel_durumlar\\uygulamalar\\cats_And_dogs\\dogs.txt'
try:
    with open(file , encoding='utf-8') as file_object:
        contents = file_object.read()
        print(contents)
        print("\n")
    with open(file2 , encoding='utf-8') as file_object2:
        contents2 = file_object2.read()
        print(contents2)
       
except FileNotFoundError:
    pass