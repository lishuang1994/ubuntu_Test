list = [3,1,89,42,84,24,57,47]
for i in range(0,len(list)-1):
    for j in range(i+1,len(list)):
        if list[i] > list[j]:
            list[i],list[j] = list[j],list[i]
    print(list)    
