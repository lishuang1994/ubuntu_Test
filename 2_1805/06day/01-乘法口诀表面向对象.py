class one():
    def two(self):
        i = 1
        while i < 10:
            j = 1
            while j <= i:
                print("%d * %d = %d"%(i,j,i*j),end = "\t")
                j += 1
            print(" ")
            i += 1
a = one()
a.two()

