#5 Lira ve Katı Parayı En Az Banknotla Veren Algoritma Denemesi
BANKNOTLAR=[0,0,0,0,0,0] #[5,10,20,50,100,200]
def BanknotSay(para):
    if para%5 !=0:
        print("5 Tl ve Katlarını yazabilirsiniz.")
        exit()
    if para >= 200:
        BANKNOTLAR[5] = int(para/200)
        para %= 200
    if para >= 100:
        BANKNOTLAR[4] = int(para/100)
        para %= 100
    if para >= 50:
        BANKNOTLAR[3] = int(para/50)
        para %= 50
    if para >= 20:
        BANKNOTLAR[2] = int(para/20)
        para %= 20
    if para >= 10:
        BANKNOTLAR[1] = int(para/10)
        para %= 10
    if para >= 5:
        BANKNOTLAR[0] = int(para/5)
        para %= 5
    return para
BanknotSay(385)
print(str(BANKNOTLAR[5])+" Tane 200 Tl lik Banknot")
print(str(BANKNOTLAR[4])+" Tane 100 Tl lik Banknot")
print(str(BANKNOTLAR[3])+" Tane 50 Tl lik Banknot")
print(str(BANKNOTLAR[2])+" Tane 20 Tl lik Banknot")
print(str(BANKNOTLAR[1])+" Tane 10 Tl lik Banknot")
print(str(BANKNOTLAR[0])+" Tane 5 Tl lik Banknot")
print(BANKNOTLAR)
