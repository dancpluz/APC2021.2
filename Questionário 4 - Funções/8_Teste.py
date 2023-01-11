def pacotesDeBolacha(bol,pes,max):
    mult = pes * max
    if mult > bol:
        print(int(bol % pes))
    else:
        print(int(bol % mult))
