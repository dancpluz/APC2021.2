def qualPeriodo(m,a,s):
    m = str(m)
    a = str(a)
    resultado = (int(a[2:4]) - int(m[0:2])) * 2 + s - int(m[3:4]) + 1

    print(resultado)

qualPeriodo(180134242,2020,0)
