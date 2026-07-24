# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        if choice != "4":
            if choice == "1":
                print("Check Balance")
                print("-"*50)
                print(f"Your Balance is :{balance}฿")
                
            elif choice == "2":
                print("Withdraw")
                print("-"*50)
                withdraw = float(input("Enter amount to withdraw :"))
                if withdraw <= balance :
                   balance = balance - withdraw
                   print(f"Your Balance is {balance}฿")
                else:
                   print(f"Not enough money.You have money {balance}฿")
                   
            elif choice == "3":
                print("Deposit")
                print("-"*50)
                deposit = float(input("Enter amount to Deposit :"))
                balance = balance + deposit
                print(f"Your Balance is {balance}฿")
                
        elif choice == "4":
                print("Thank You!")
                break
else:
    print("Invalid PIN")