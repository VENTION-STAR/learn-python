#for循环
#1.迭代对象为列表
temp = [26,69,85,12,48]
for t in temp :
    print(t)
#2.对象为字符串
words = "hello world !"
for word in words :
    print(word)
#3.字典
#from dictionary import vocaloid_singers
#for k in vocaloid_singers.keys() :
#    print(k)
#4.range(初始值，结束值，步幅）
io=0
for i in range(1,101) :
    io=io+i
print(io)