#计算BMI:体重/（身高**2）
体重 = int(input("请输入体重（千克）"))
身高 = float(input("请输入身高（米）"))
BMI = str(体重/(身高**2))
print("你的BMI是："+BMI)
#判断bmi类型
bmi = float(BMI)
if bmi <= 18.5 :
    print("你的体重偏廋")
elif bmi <= 25 :
    print("你的体重正常")
elif bmi <= 30 :
    print("你的体重偏胖")
elif bmi > 30 :
    print("你的体型肥胖")