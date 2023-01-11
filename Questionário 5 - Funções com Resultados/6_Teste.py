def multiplo5(n):
    if n == 0:
        return True
    elif n == 1 or n == 2 or n == 3 or n== 4:
        return False
    else:
        return multiplo5(n-5)

def não_multiplo5(n):
    if n == 0:
        return False
    elif n == 1 or n == 2 or n == 3 or n == 4:
        return True
    else:
        return não_multiplo5(n-5)
