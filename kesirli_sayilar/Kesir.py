class Kesir:
    def __init__(self,pay,payda):
        self.pay = pay
        self.payda = payda

    def __str__(self):
        return str(self.pay)+"/"+str(self.payda)

    def __add__(self,diger):
        yenipay = self.pay * diger.payda + \
            self.payda * diger.pay
        yenipayda = self.payda * diger.payda
        return Kesir.sadelestir(Kesir(yenipay,yenipayda))

    def __sub__(self,diger):
        return Kesir.sadelestir(self+Kesir(-1,1)*diger)

    def __mul__(self,diger):
        return Kesir.sadelestir(Kesir\
            (self.pay*diger.pay,self.payda*diger.payda))

    def __truediv__(self,diger):
        return Kesir.sadelestir\
            (Kesir(self.pay*diger.payda,self.payda*diger.pay))

    def __pow__(self,diger):
        if type(diger) == type(self):
            return Kesir.sadelestir(Kesir(pow(self.pay,Kesir.floatyap(diger)),\
                pow(self.payda,Kesir.floatyap(diger))))
        else:
            return Kesir.sadelestir(Kesir(pow(self.pay,diger),\
                pow(self.payda,diger)))

    def __lt__(self,diger):
        return Kesir.floatyap(self)<Kesir.floatyap(diger)

    def __le__(self,diger):
        return Kesir.floatyap(self)<=Kesir.floatyap(diger)

    def __eq__(self,diger):
        return Kesir.floatyap(self)==Kesir.floatyap(diger)

    def __ne__(self,diger):
        return Kesir.floatyap(self)!=Kesir.floatyap(diger)

    def __ge__(self,diger):
        return Kesir.floatyap(self)>=Kesir.floatyap(diger)

    def __gt__(self,diger):
        return Kesir.floatyap(self)>Kesir.floatyap(diger)

    def floatyap(self):
        return self.pay/self.payda

    def sadelestir(self):
        if Kesir.EBOB(self.pay,self.payda)>1:
            ebob = Kesir.EBOB(self.pay,self.payda)
            return Kesir(self.pay/ebob,self.payda/ebob)
        else:
            return Kesir(self.pay,self.payda)

    def EBOB(a,b):
        while a%b != 0:
            eski_a = a
            eski_b = b
            a = eski_b
            b = eski_a%eski_b
        return b
