#使用列表创建购物清单
shopping_list = ["pico 4pro","rx 6750 gre"]
#添加龙年fufu
shopping_list.append(input("还要买什么："))
#没钱买6750，不要了
shopping_list.remove(shopping_list[1])
#看看有几个元素
print("一共买了"+str(len(shopping_list))+"件东西")
#把要买的打印出来
print(shopping_list)



