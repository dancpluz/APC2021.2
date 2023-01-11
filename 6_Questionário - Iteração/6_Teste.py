a,b,c = input().split()
a1 = int(a)
q = int(b)
n = int(c)
i = 1

while n >= i:
    print(a1 * q ** (i-1))
    i += 1

print(int((a1 * (q ** n - 1))/(q - 1)))
