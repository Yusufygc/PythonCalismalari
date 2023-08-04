def count_words(filename):
    try:
        with open(filename,encoding='utf-8') as f:
            content=f.read()
    except FileNotFoundError:
        print(f"{filename} dosyası bulunamadı.")
    else:
        words=content.split()
        num_words=len(words)
        print(f"{filename} dosyasında yaklaşık {num_words} kelime var.")

filenames=["ozel_durumlar_ve_TryExcept\\alice.txt","ozel_durumlar_ve_TryExcept\\modick.txt"]
for filename in filenames:
    count_words(filename)