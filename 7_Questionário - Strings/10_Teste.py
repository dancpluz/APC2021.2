def não_possui_a_letra_u(palavra):
    for letra in palavra:
        if letra.lower() == 'u':
            return False
        elif letra.lower() == 'ú':
            return False
        elif letra.lower() == 'ù':
            return False
        elif letra.lower() == 'û':
            return False
        elif letra.lower() == 'ü':
            return False
    return True
