def area(arg1,arg2,forma):
    if forma == "retangulo":
        resultado = int(arg1 * arg2)
    elif forma == "triangulo":
        resultado = int(arg1 * arg2 / 2)
    elif forma == "losango":
        resultado = int(arg1 * arg2 / 2)
    elif forma == "circulo":
        resultado = int(arg2 * arg1 ** 2)

    print(f'O {forma} tem {resultado} de area')
