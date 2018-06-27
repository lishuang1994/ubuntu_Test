id_card = {"name":"李爽","birthday":"1994.03.25","address":"辽宁","eth":"汉","sex":"女"}
print(id_card)
print(type(id_card))
id_card["birthday"] = "1991.08.20"
print(id_card)
print(id_card["name"])
id_card["name"] = "耐克"
print(id_card)
#id_card.popitem()#随机删除，字典是无序的
#print(id_card)
id_card.pop("name")
print(id_card)
del id_card["name"]

