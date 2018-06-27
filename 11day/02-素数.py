list = []
b = 0
for i in range(100,201):
    flag = 10
    for j in range(2,i):
        if i%j == 0:
            flag = 0
            break
    if flag == 10:
        print(i) 
    a+=1
    a = i + 
