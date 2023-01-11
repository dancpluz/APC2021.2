import math

def acredita(n1,n2):
    d = n1 / n2
    log = math.log(d,n2)
    
    if log % 1 >= 0.001:
        return "Fake News"
    else:
        return "Pode Acreditar"



print(acredita(8,2))
print(acredita(18,3))
print(acredita(625,5))
