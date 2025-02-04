平均值 = 0
i = 0
sum = 0
输入 = input()
while 输入 != 'q' :
    sum = sum + int(输入)
    i=i+1
    输入 = input()
if i==0 :
    print('推出成功')
else :
    平均值 = sum/i
    print(平均值)