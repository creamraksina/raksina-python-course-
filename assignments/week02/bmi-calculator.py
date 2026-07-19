print("-"*50)
print("BMI CALCULATOR")
print("-"*50)

weight = float(input("Enter your weight (Kg) : "))
height = float(input("Enter your height (M) : "))

BMI = weight / (height**2)

print(f"Your BMI is {BMI:.1f}\n")
print("-"*50)
print("BMI CATEGORIES")
print("-"*50)
print("Below 18.5: Underweight.")
print("18.5 - 24.9: Normal weight.")
print("25.0 - 29.9: Overweight.")
print("30.0 and above: Obese.")
print("-"*50)

if BMI < 18.5:
    print("Your is Underweight.")
elif BMI >= 18.5 and BMI <= 24.9:
    print("Your is Normal weight.")
elif BMI >= 25.0 and BMI <= 29.9:
    print("Your is Overweight.")
elif BMI >= 30.0:
    print("Your is Obese.")
    
