def binario(n, exp):
    exp = exp + 1
    if n == 0:
        return
    else:
        binario(n // 2, exp)
        print(f'{n%2}*(2**{exp})', end="")
        if exp > 0:
            print(f' + ', end="")
        exp = exp - 1
