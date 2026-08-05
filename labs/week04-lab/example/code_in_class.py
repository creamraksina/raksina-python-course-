# รับชื่อจริง (หรือข้อความ) จากผู้ใช้
# นับจำนวนสระทั้งหมดในข้อความนั้นว่ามี (a,e,i,o,u) 

#ตัวอย่างหน้าจอ
# What is your name? : Boonchoo
# Your taxt have 4 vowels.

name = input(" What is your name? : ")
letters = list(name)
print(letters)

count = 0

for letters in name:
    if letters == "a" or letters == "A":
        count = count + 1
    if letters == "e" or letters == "E":
        count = count + 1
    if letters == "i" or letters == "I":
            count = count + 1
    if letters == "o" or letters == "O":
            count = count + 1
    if letters == "u" or letters == "U":
            count = count + 1
            
print(f"Your taxt have {count} vowels.")