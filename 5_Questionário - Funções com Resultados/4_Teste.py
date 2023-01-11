a = input()

def maiorQue1000(a):
    if a > 1000:
        return a
    else:
        maiorQue1000(a**2)

maiorQue1000(a)
