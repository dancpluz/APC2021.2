def triangulo(x,size):
    if size <= 0:
        return
    else:
        print(" " * x + "*" * size)
        return triangulo(x+1,size-2)
