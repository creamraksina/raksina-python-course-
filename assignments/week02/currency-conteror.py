print("-"*50)
print("CURRENCY CONVERTER")
print("-"*50)

print("Plese choose conversion direction ")
print("1.THB to USD")
print("2.USD to THB")
choice = int(input("Enter your choice : "))

if choice == 1:
    THB = float(input("Enter amount to convert (THB) : "))
    USD = THB / 35.5
    print(f"USD = {THB} / 35.5")
    print(f"USD = {USD:.2f}")
    print(f"{THB:.2f} THB to USD is {USD:.2f} USD.")
elif choice == 2:
    USD = float(input("Enter amount to convert (USD) : "))
    THB = USD * 35.5
    print(f"THB = {USD} * 35.5")
    print(f"THB = {THB:.2f}")
    print(f"{USD:.2f} USD to THB is {THB:.2f} THB.")
else:
    print("Plese choose conversion direction between 1 or 2")
 