m = input("请输入性别")
if m == "男":
    a = int(input("请输入身高"))
    b = int(input("请输入财富"))
    c = int(input("请输入颜值"))
    if a>180 and b>1000 and c>90:
        print("高富帅")
    else:
        print("稳住,别哭")

if m == "女":
    d = input("请输入皮肤颜色")
    e = int(input("请输入财富"))
    f = int(input("请输入颜值"))
    if d=="白色" and e>800 and f>90:
        print("白富美")
    else:
        print("哈哈哈")
