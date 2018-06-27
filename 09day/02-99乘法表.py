i = 1
while i < 10:
    j = 1
    while j <= i:
        d = i * j
        print("%d * %d = %d"%(i,j,d), end = "\t ")
        j+=1
    print(" ")
    i+=1
