path = "dosya_okuma_islemi\\uygulama.txt"
"""
with open(path) as file_object:
    contents=file_object.read()
    for i in range(0,3):
        print(contents.rstrip())

######################################
with open(path) as file_object:
    lines=file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))"""
######################################
with open(path) as file_object:
    lines=file_object.readlines()
    for line in lines:
        new_line = line.replace('python', 'c')
        print(new_line.rstrip())

