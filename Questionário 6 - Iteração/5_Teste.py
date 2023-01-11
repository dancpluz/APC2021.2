def Primo(x):
    i = 2
    while i < x:
        if x % i == 0:
            return False
        i += 1
    return True

n = int(input())
cont = 1
x = 2
mult = 1

while cont <= n:
    if Primo(x):
        mult *= x
        cont += 1
    x += 1

print(mult)
