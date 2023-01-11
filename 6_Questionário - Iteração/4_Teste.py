while True:
    n = int(input())
    if n == 42:
        print("Você acertou!")
        break
    elif n > 42:
        print("Tenta dar uma diminuída")
    else:
        print("É maior que isso")
