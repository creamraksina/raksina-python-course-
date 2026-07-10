print("1. Circle Calculator:")
print("   - Ask user for radius")
print("   - Calculate area (π * r²)")
print("   - Calculate circumference (2 * π * r)")
print("   - Use 3.14159 for π")
print("_"*50)
print()
#input
redius = float(input("Redius: "))
#processs
area = 3.14159 * redius ** 2
circumference = 2 * 3.14159 * redius
#output
print(f"Area of this Circle : {area}") #{area:.2f} การ Fix ให้ออกมาแค่ทศนิยม 2 ตำแหน่ง
print(f"Circumference of this Circle : {circumference}")

print("_"*50)
print()

