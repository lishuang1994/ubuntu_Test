def cul_num(num):
    if num == 1:
        return 1
    else:
        return num*cul_num(num-1)
rus = cul_num(5)
print(rus)
