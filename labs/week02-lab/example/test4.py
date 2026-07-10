print("4. BMI Calculator:")
print("   - Ask for weight (kg) and height (m)")
print("   - Calculate: BMI = weight / (height ** 2)")
print("_"*50)
print()

#input
weight = float(input("Enter your Weight (Kg) : "))
height = float(input("Enter your Height (M) : "))

#processs
BMI = weight / (height ** 2)

#output
print(f"Your BMI is {BMI:.2f}.")