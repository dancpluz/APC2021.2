def nota(p1,p2,p3,s,n1,n2):
    media1 = n1*p1
    media2 = n2*p2
    soma_pesos = p1+p2+p3

    if s == 'MM':
        return (-media1 - media2 + 5 * soma_pesos) / p3
    elif s == 'MS':
        return (-media1 - media2 + 7 * soma_pesos) / p3
    elif s == 'SS':
        return (-media1 - media2 + 9 * soma_pesos) / p3
