#manter verificação se a == b
#achar se a pode ser igual a b (in)
#if sim, decidir o que fazer para chegar lá .find()
#if .find() for maior q a metade len() remover as primeiras letras
#else remover ultimas
#cada removida count+1

a = input()
b = input()
count = 0

if b in a:
    list = a.split(b)
    str = ''.join(list)
    print(len(str)+count)
elif a in b:
    list = b.split(a)
    str = ''.join(list)
    print(len(str)+count)
else:
    pass
