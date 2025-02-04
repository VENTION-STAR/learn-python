#计算BMI:体重/（身高**2）
体重 = int(input("请输入体重（千克）"))
身高 = float(input("请输入身高（米）"))
BMI = str(体重/(身高**2))
print("你的BMI是："+BMI)