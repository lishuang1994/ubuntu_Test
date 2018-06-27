i = 0
while i < 10:
    j = 0
    while j < i:
        d = i * j
        print("%d * %d = %d"%(i,j,d),end = "\t")
        j+=1
    print(" ")
    i+=1
