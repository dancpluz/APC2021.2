n = int(input())

while n > -1:
    if n == 0:
        print("Ué? Já acabou?")
    elif n % 2 == 0:
        print("Bom dia!")
    else:
        print("Boa noite!")
    n -= 1
