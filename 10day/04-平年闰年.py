year = int(input("请输入年份"))
if year %4 == 0 and year %100 !=0:
    print("%d闰年"%year)
elif year %400 == 0:
    print("%d闰年"%year)
else:
    print("%d平年"%year)
