def impar(n):
    if n % 2 == 0:
        return False
    else:
        return True

x = int(input())
acumulador = 0
cont = 0

while x >= 0:
    if impar(x):
        acumulador = acumulador + x
        cont += 1
    x = int(input())

if cont == 0:
    print(0.0)
else:
    media_impar = acumulador/cont
    print(media_impar)
