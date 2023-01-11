def delta(a,b,c):
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        return "Essa equacao possui duas raizes distintas"
    elif delta < 0:
        return "Essa equacao nao possui raizes reais"
    elif delta == 0:
        return "Essa equacao possui duas raizes iguais"
