import csv

with open(input(),'r') as f:
    reader = csv.reader(f)
    cabeca = []
    for row in reader:
        if cabeca == []:
            cabeca = row[1:]
        else:
            valores = [float(i) for i in row[1:]]
            index = valores.index(min(valores))
            print(row[0],cabeca[index])
