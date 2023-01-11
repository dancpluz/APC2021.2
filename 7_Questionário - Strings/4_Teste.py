def tem_letra_maiúscula(s): #função para checar se possui alguma letra maiúscula
    for letra in s: #loop para iterar na string
        if letra.isupper(): #checa se a letra é maiúscula
            return True #se for o programa acaba e retorna True
    return False #depois do loop se nenhuma letra for maiúscula retorna False
