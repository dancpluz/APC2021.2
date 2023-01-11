def calcula_tiquete_estacionamento(chegada_h,chegada_min,saida_h,saida_min):
    horas = saida_h - chegada_h

    if horas < 0:
        horas += 24

    minutos = saida_min - chegada_min
    horas_cheias = (horas * 60 + minutos) / 60

    if horas_cheias % 2 != 0:
        horas_cheias = int(horas_cheias) + 1

    if horas_cheias == 0:
        return 3.5,1
    elif horas_cheias == 1:
        return 3.5, 1
    elif horas_cheias == 2:
        return 7, 2
    elif horas_cheias == 3:
        return 7 + 4.1, 3
    elif horas_cheias == 4:
        return 7 + 8.2, 4
    elif horas_cheias > 4:
        return 7 + 8.2 + (horas_cheias - 4) * 4.6, int(horas_cheias)

print(calcula_tiquete_estacionamento(8,0,0,0))
print(calcula_tiquete_estacionamento(8,10,0,0))
print(calcula_tiquete_estacionamento(8,10,18,0))
print(calcula_tiquete_estacionamento(8,15,10,32))
print(calcula_tiquete_estacionamento(10,10,10,45))
print(calcula_tiquete_estacionamento(23,45,0,30))
