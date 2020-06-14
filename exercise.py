weight = input("请输入体重(kg):" )
height = input("请输入身高(m):")

weight = float(weight)
height = float(height)

bmi = weight / height **2
bmi = float(bmi)

if bmi < 18.5:
	print("体重过轻")
elif bmi >= 18.5 and bmi < 24:
	print("正常范围")
elif bmi >= 24 and bmi < 27:
	print("体重过重")
elif bmi >= 27 and bmi < 30:
	print("轻度肥胖")
elif bmi >= 30 and bmi < 35:
	print("中度肥胖")
elif bmi >= 35:
	print("重度肥胖")