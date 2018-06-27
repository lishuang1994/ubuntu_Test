list = []
def num():
    for i in range(2,201):
        d = 0
        for j in range(2,i):
            if i % j == 0:
                d = 1
                break
        if d == 0:
            list.append(i)
    return list
r = num()
print(r)
