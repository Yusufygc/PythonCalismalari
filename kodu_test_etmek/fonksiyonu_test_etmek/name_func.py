"""
def get_name(first,middle,last): # middle ı ekleyerek başarısız testi görelim
    full_name = first + ' ' + last
    return full_name.title()
"""
# middle eklenince hata verdi ve test başarısız oldu. Başarısızlığı gidermek için middle ı opsiyonel yapalım

def get_name(first,last,middle=""): # middle ı opsiyonel yaptık. (middle="") ile

    if middle:
        full_name =f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()






