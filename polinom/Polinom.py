from copy import deepcopy
class Polinom:
    def __init__(self,*args):
        self.katsayilar = []
        for katsayi in args:
            self.katsayilar.append(katsayi)
        self.baskatsayi = katsayi

    def __str__(self):
        yazi = ""
        i = len(self.katsayilar)-1
        for katsayi in reversed(self.katsayilar):
            if i == len(self.katsayilar)-1:
                yazi+=str(katsayi)+"x^"+str(i)
            elif katsayi != 0:
                if i > 1:
                    yazi+=" + "+str(katsayi)+"x^"+str(i)
                elif i == 1:
                     yazi+=" + "+str(katsayi)+"x"
                else:
                    yazi+=" + "+str(katsayi)
            i-=1
        return yazi

    def __add__(self,diger):
        if type(diger) == type(0): #Integer ise
            sonuc = deepcopy(self)
            sonuc.katsayilar[0] += diger
            return sonuc
        elif type(diger) == type(self):
            if len(self.katsayilar) >= len(diger.katsayilar):
                buyuk = deepcopy(self)
                kucuk = deepcopy(diger)
            else:
                buyuk = deepcopy(diger)
                kucuk = deepcopy(self)
            for i in range(len(kucuk.katsayilar)):
                buyuk.katsayilar[i] += kucuk.katsayilar[i]
            return buyuk
        else:
            print("Polinomlar sadece bir başka polinom \
                yada tamsayı ile toplanabilir")
            return self


    def __sub__(self,diger):
        if type(diger) == type(0): #Integer ise
            return self+(-1)*diger
        elif type(diger) == type(self):
            eski = []
            i = 0
            for _ in range(len(diger.katsayilar)):
                eski.append(0)
            for kat in diger.katsayilar:
                eski[i] = -kat
                i+=1
            return self+Polinom(*eski)
        else:
            print("Polinomlar sadece bir başka polinom \
                yada tamsayı ile eksiltilebilir.")
            return self

    def __mul__(self,diger):
        if (type(diger) == type(0)):
             sonuc = deepcopy(self)
             for i in range(len(sonuc.katsayilar)):
                 sonuc.katsayilar[i] *= diger
             return sonuc
        elif type(diger) == type(self):
            carpilmis = []
            for _ in range(len(self.katsayilar)+len(diger.katsayilar)-1):
                carpilmis.append(0)
            for i in range(len(self.katsayilar)):
                for j in range(len(diger.katsayilar)):
                    carpilmis[i+j] += self.katsayilar[i] * diger.katsayilar[j]
            return Polinom(*carpilmis)
        else:
            print("Polinomlar sadece bir başka polinom \
                yada tamsayı ile çarpılabilir.")
            return self
