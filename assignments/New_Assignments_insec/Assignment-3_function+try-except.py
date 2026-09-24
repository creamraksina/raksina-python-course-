def deposit(money):
    global total
    
    try:
        money = float(input("กรอกจำนวนยอดเงินที่จะฝาก :"))
        if money <= 0 :
            raise ValueError("จำนวนเงินฝากต้องมากกว่า 0")
        
        total = total + money    
        
    except ValueError as error:
        print(f"เกิดข้อผิดพลาด :{error}")
    else:
        print("\n")
        print("ฝากเงินสำเร็จ")
        print(f"ยอดเงินคงเหลือ : {total:.2f} บาท")
    finally:
        print("สิ้นสุดรายการฝากเงิน")

total = 1000  

print(f"ยอดเงินเริ่มต้น : {total:.2f}")
money = 0
deposit(money)