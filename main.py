#6-m
class Telefon:
    def __init__(self, model):
        self.model = model
        
    def qongiroq(self):
        print("Qo'ng'iroq qilinmoqda")
        

class Smartphone(Telefon):
    def qongiroq(self):
        super().qongiroq()
        print(f"Video Qo'ng'iroq")
        
u1 = Telefon("Iphone")
u1.qongiroq()
