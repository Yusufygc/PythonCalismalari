class Restorant:
    def __init__(self,restoran_adı,mutfak_türü):
        self.restoran_adı=restoran_adı
        self.mutfak_türü=mutfak_türü
        self.servis_sayısı=0

    def tanıtım(self):
        print(f"{self.restoran_adı} restoranı {self.mutfak_türü} mutfağındadır")   

    def servis_sayısını_güncelle(self,servis):
        self.servis_sayısı=servis
        print(f"servis sayısı {self.servis_sayısı} olarak güncellendi")
    
    def servis_yapılan_müşteri_sayısı(self,servis):
        self.servis_sayısı += servis
        print(f"servis yapılan müşteri sayısı {self.servis_sayısı} olarak güncellendi") 

    def servis_yapılan_müşteri_sayısı_artır(self,servis):
        self.servis_sayısı += servis
        print(f"servis yapılan müşteri sayısı {self.servis_sayısı} olarak güncellendi")
        
class Dondurma(Restorant):
    def __init__(self, restoran_adı, mutfak_türü):
        super().__init__(restoran_adı, mutfak_türü)
        self.dondurma_türleri=["çikolata","vanilya","çilek","muzlu","fıstıklı"]
    
    def Aroma(self):
        print("dondurma aromaları : ")
        for dondurma in self.dondurma_türleri:
            print(f"\t\t\t{dondurma}")