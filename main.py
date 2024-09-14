height = int(input("Enter height:"))
weight = float(input("enter weight:"))
BMI = weight/(height/100)**2
print("your BMI is :", BMI)

if BMT <=18.4:
    print("underweight")
elif BMI <=34.9:
    print("over weight")
else:
    print("obese")