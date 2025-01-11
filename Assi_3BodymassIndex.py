weight = int(input("Enter yor weight in kg: "))
height = float(input("Enter your height in meter: "))
BMI= weight/(height * height)
if BMI < 18.5:
    print("You are underweight")
elif 18.5 <= BMI <= 24.9:
    print("You are normal")
elif 25 <= BMI <= 29.9:
    print("You are overweight")
else:
    print("You are obese") 
