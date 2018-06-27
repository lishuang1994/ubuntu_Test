list = [1,100,49,10,56,3,2,37]
#enumerate找
count = 3
for p,v in enumerate(list):
    if count == v:
        print(p)
#index 找
zz = list.index(count)
print(zz)
#while
i = 0
while i < len(list):
    if list[i] == 3:
        print("索引是%d"%i)
        break
    i+=1
#二分法找
list = [1,4,7,24,45,49,62,73]
min = 0
max = len(list)-1
count = 62
while True:
    center = int((min + max)/2)#中间
    if list[center] > count:
        max = center - 1
    if list[center] < count:
        min = center + 1
    elif list[center] == count:
        print("索引是%d"%center)
        break
