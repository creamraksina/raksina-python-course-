"""
เขียน Function แปลงหน่วยสกุลเงิน ที่สามารถแปลจากค่าเงิน

THB <--> USD ... 1 USD = 32 THB
THB <--> JPY ... 100 JPY = 22 THB

โดยใช้ชื่อ Function convert_currency(100,"USD")

แสดงผลออกทางหน้าจอ
100 THB = 3.3 USD

และทดสอบการใช้งาน Function ที่ตัวเองเขียนด้วย
"""

def convert_currency_USD(amount,currency):
    if currency == "USD":
        total = amount / 32.0
        print(f"{amount:.2f} THB = {total:.2f} USD")
    else:
        total = amount * 32.0
        print(f"{amount:.2f} USD = {total:.2f} THB")
    
def convert_currency_JPY(amount,currency):
    if currency == "JPY":
        total = amount / 22.0
        print(f"{amount:.2f} THB = {total:.2f} JPY")
    else:
        total = amount * 22.0
        print(f"{amount:.2f} JPY = {total:.2f} THB")
  
convert_currency_USD(100,"USD")  
convert_currency_JPY(100,"JPY")

  
  
    
"""
while True:
    print("Enter your Choice to convert currency.")
    print("1.Convert currency USD.")
    print("2.Convert currency JPY.")
    print("3.Exit")
    choice = int(input("Enter choice: "))
    if choice == "1":
        convert_currency_USD()
        
    elif choice == "2":
        convert_currency_JPY()
        
    elif choice == "3":
        break
"""
        
        
    
