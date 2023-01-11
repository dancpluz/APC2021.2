import math

def calcula_tratamento_numeros(a,b):
    potencia_ab = a**b
    potencia_ba = b**a
    maior_ab = max(a,b)
    parte_inteira_a = int(a)
    parte_frac_a = round(a)
    parte_inteira_b = int(b)
    parte_frac_b = round(b)

    print(f'{a} elevado a {b} eh {potencia_ab:.2f}')
    print(f'{b} elevado a {a} eh {potencia_ba:.2f}')
    print(f'O maior entre {a} e {b} eh {maior_ab}')
    print(f'A parte inteira de {a} eh {parte_inteira_a}')
    print(f'A parte fracionaria de {a} eh {parte_frac_a:.2f}')
    print(f'A parte inteira de {b} eh {parte_inteira_b}')
    print(f'A parte fracionaria de {b} eh {parte_frac_b:.2f}')

def calcula_area_geometrica(a,b):
    area_quadrado_a = a*a
    area_quadrado_b = b*b
    area_circulo_a = math.pi * a * a
    area_circulo_b = math.pi * b * b

    print(f'O quadrado de lado {a} tem area de tamanho {area_quadrado_a:.2f}')
    print(f'O quadrado de lado {b} tem area de tamanho {area_quadrado_b:.2f}')
    print(f'O circulo de raio {a} tem area de tamanho {area_circulo_a:.2f}')
    print(f'O circulo de raio {b} tem area de tamanho {area_circulo_b:.2f}')
