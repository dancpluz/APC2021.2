def JaChegou(n,s):
    if n == 0:
        return
    else:
        print(s)
        return JaChegou(n-1,s)
