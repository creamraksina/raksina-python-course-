def deposit(money):
    global total
    
    try:
        money = float(input("กรอกจำนวนยอดเงินที่จะฝาก :"))
        
        if money <= 0 :
            raise ValueError("จำนวนเงินฝากต้องมากกว่า 0")

        total = total + money
        
    except ValueError as error:
        print(f"เกิดข้อผิดพลาด กรุณากรอกจำนวนยอดเงินใหม่อีกครั้ง :{error}")
    else:
        print("ฝากเงินสำเร็จ")
        print(f"ยอดเงินคงเหลือ : {total:.2f} บาท")
    finally:
        print("สิ้นสุดรายการฝากเงิน")

total = 1000
choice=0 
i=1
while choice != 4:
    print("---------------------") 
    print("      ระบบฝากเงิน      ")
    print("---------------------")
    print("1.ฝากเงิน\n2.ถอนเงิน\n3.ตรวจสอบยอดเงิน\n4.Exit")
    
    choice = int(input("Enter Menu :")) #รับค่า input เพื่อตรวจสอบเงื่อนไขลูป 
    if choice != 4:#ถ้ารับค่ามาไม่เท่ากับ 4 ก็ในทำในคำสั่งต่อไปนี้
        if choice == 1:
            money = 0
            deposit(money)    
            
            
        elif choice == 2:
            money = float(input("กรอกจำนวนยอดเงินที่จะถอน :"))
            if money <= total:
                total = total-money
            else:
                print("ยอดเงินคงเหลือไม่พอในการให้บริการ","คุณมียอดคงเหลือ",total)  
                
                  
        elif choice == 3:
            print("คุณมียอดคงเหลือในบัญชี",total)  
    print("ขอบคุณที่ใช้บริการ โอกาสน่าเชิญใหม่")        
