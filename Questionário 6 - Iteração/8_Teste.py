def primo(n):
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True

def goldao(n):

    for p1 in range(2, n):
        if primo(p1) and primo(n-p1):
            p2 = n-p1
            return p1,p2

print(goldbach(8))
