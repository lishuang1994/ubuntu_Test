import random
all_money = 0
km = random.randint(1,100)
for i in range(1,31):
    for j in range(1,3):
        if km <= 6:
            price = 3
        if km > 6 and km <= 12:
            price = 4
        if km > 12 and km <= 22:
            price = 5
        if km > 22 and km <= 32:
            price = 6
        if km > 32:
            if (km-32)%20 == 0:
                price = 6+(km-32)/20
            else:
                price = 6+int((km-32)/20)+1
        if all_money > 100 and all_money <= 150:
            price = price * 0.8
        if all_money > 150:
            price = price * 0.5
        all_money = all_money + price
print("乘车总额%0.2f"%all_money)
