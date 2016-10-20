def EBOB(a,b):
    ebob = 1
    if a<b:
        kucuk = a
    else:
        kucuk = b
    i = 2
    while i < kucuk+1:
        if (a%i == 0) and (b%i == 0):
            ebob = ebob*i
            a = a/i
            b = b/i
            kucuk = kucuk/i
            i = i-1
        i = i+1
    return ebob

a = 22222222
b = 33333333
print(EBOB(a,b))
