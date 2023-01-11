def não_possui_a_letra_e(palavra):
    for letra in palavra:
        if letra.lower() == 'e':
            return False
        elif letra.lower() == 'é':
            return False
        elif letra.lower() == 'ê':
            return False
        elif letra.lower() == 'è':
            return False
    return True
