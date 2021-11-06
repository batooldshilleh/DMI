height = float(input("enter your hight in m :  "))
weight = float(input("enter your weight in kg :  "))
bmi = round( weight /(height ** 2))
print(f"your bmi is {bmi}")
if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi<25:
    print("normal weight")
elif bmi >=25 and bmi <30:
    print("overweight")
elif bmi >=30 and bmi <35 :
    print("obese")
else :
    print("clinically obese")
