def listaValoresUnicos(lista):
    unicos = []
    for item in lista:
        if item in unicos:
            pass
        else:
            unicos += [item]
    return unicos
