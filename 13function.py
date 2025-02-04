def calculate_bmi(w,h) :
    bmi = w /(h**2)
    if bmi <= 18.5 :
        print("您的bmi分类为偏瘦")
    elif bmi <= 25 :
        print("您的bmi分类为正常")
    elif bmi <= 30 :
        print("您的bmi分类为偏胖")
    else :
        print("您的bmi分类为肥胖")
    return bmi
bmi_1 = calculate_bmi(90,1.75)
print(bmi_1)