def escada(n):
    if n == 0:
        return
    else:
        escada(n-1)
        print("#" * n)
