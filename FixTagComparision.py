def orderComparision(order1,order2):
    print("order1"+str(order1))
    print("order2" + str(order2))
    print("Difference in parameter")
    o1=order1.split("|")
    o2 = order2.split("|")
    for a,b in zip(o1,o2):
        if a!=b:
            print("order1:"+str(a),"order2:"+str(b))

orderComparision("55=DMART|44=504|38=10|1=ICIC_1","55=DMART|44=502|38=10|1=HDFC_1")
