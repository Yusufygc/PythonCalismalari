filename = 'programming.txt'

with open(filename,'w') as file_object:
    file_object.write("programlamayi severim!!")
    file_object.write("\npython programlama dili")
    file_object.write("\nC programlama dili")
    
with open(filename,'a') as file_object: # append modu sonuna ekleme yapar
    file_object.write("\nC++ programlama dili")
    file_object.write("\njava programlama dili")