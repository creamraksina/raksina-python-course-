
"""
1. รับค่า Text จากผู้ใช้
2. รับค่าอักขระที่ต้องการจากผู้ใช้
3. แสดงผลจำนวนของอักขระในข้อความ text

ตัวอย่างการแสดงหน้าจอ
Insert Your Text : Boonchoo Jitnupong
Character 'o' found in 'Boonchoo Jitnupong'
"""

"""
print("\n=== ITERATING THROUGH STRING ===") # เป็นการให้หาแบบเลือกได้ว่าเราจะให้หาตัวอักษรอะไร
count = 0
text = input("Insert Your Text: ")
char = input("Input Character to find : ")
for letter in text:
    if letter == char: #if letter == 'o'or letter =='O': ตรวจทั้งตัวพิมพ์ใหญ่และเล็ก
        count += 1
        
print(f"{count} letters {char} found in '{text}'")
"""



"""
1. เขียนโปรแกรมตรวจสอบความแข็งแรงของ Password
2. นิยามของ Strong password คือ ยาวมากกว่า 8 , มีอักขระ @ 1 ตัว , มีตัวเลข , มีตัวอักษร 

ตัวอย่างการแสดงหน้าจอ
Insert your password : Boonchoo
Your passeord is not strong!!

Insert your password : Test@123
Your passeord is strong!
"""

print("\n=== STRONG PASSWORD ===")
password = input("Insert your password : ")
lenght = len(password)
words = password.split('@')

if len(words) > 1 and password.count('@') == 1 :
    left = words[0].isalnum()
    right = words[1].isalnum()
else :
    left = False;
    right = False;
    
if lenght >= 8 and len(words) == 2 and left == True and right == True:
    print("Your password is strong!")
else:
    print("Your passeord is not strong! ")