fruits = ["apple", "banana", "orange", "grape", "kiwi"]

# Positive indexing (0-based)
print(f"First fruit: {fruits[0]}")      # apple #แสดงตัวที่ index อยู่
print(f"Second fruit: {fruits[1]}")     # banana
print(f"Last fruit: {fruits[4]}")       # kiwi

# Negative indexing
print(f"Last fruit: {fruits[-1]}")      # kiwi
print(f"Second last: {fruits[-2]}")     # grape

# List slicing
print(f"First 3 fruits: {fruits[0:3]}")     # ['apple', 'banana', 'orange'] # ดึงแค่ index 0 - 2
print(f"From index 2: {fruits[2:]}")        # ['orange', 'grape', 'kiwi'] #สองยาวไปจนหมด
print(f"Last 2 fruits: {fruits[-2:]}")      # ['grape', 'kiwi'] 
print(f"Every 2nd fruit: {fruits[::2]}")    # ['apple', 'orange', 'kiwi'] #เชือนตั้งแต่ตัวแรกไปจนสุดท้าย โดดทีละสอง
print(f"Reverse list: {fruits[::-1]}")      # ['kiwi', 'grape', 'orange', 'banana', 'apple'] # ทุกตัวแบบย้อนกลับ

# Changing single elements
fruits = ["apple", "banana", "orange"]
fruits[1] = "mango" #แก้ไขข้อมูลใน index เบอร์ 1
print(fruits)  # ['apple', 'mango', 'orange'] มีหน้าตาเปลี่ยนไป

# Changing multiple elements
fruits[0:2] = ["pear", "cherry"] # เปลี่ยนข้อมูลตั้งแต่ index 0 ไปถึง 1 ** 2-1 อย่าลืม
print(fruits)  # ['pear', 'cherry', 'orange']

# Adding elements
fruits.append("grape")           # Add to end เพิ่มต่อท้าย
print(fruits)  # ['pear', 'cherry', 'orange', 'grape']

fruits.insert(1, "banana")       # Insert at specific position แทรกเข้าไปใน index 1
print(fruits)  # ['pear', 'banana', 'cherry', 'orange', 'grape']

fruits.extend(["kiwi", "apple"]) # Add multiple elements เพิ่มข้อมูลทีละหลายตัว เข้าด้านหลัง
print(fruits)  # ['pear', 'banana', 'cherry', 'orange', 'grape', 'kiwi', 'apple']

# Removing elements
fruits.remove("banana")          # Remove first occurrence เจอ banana ตัวแรก เอาออก
print(fruits)  # ['pear', 'cherry', 'orange', 'grape', 'kiwi', 'apple']

removed_fruit = fruits.pop()     # Remove and return last element       การ pop มาเป็บไว้ในตัวแปร มีการใช้แบบบ่งบอกตำแหน่ง ถ้าไม่ระบุจะเป็นการลบหลังสุด
print(f"Removed: {removed_fruit}")  # apple
print(fruits)  # ['pear', 'cherry', 'orange', 'grape', 'kiwi']

removed_fruit = fruits.pop(1)    # Remove and return element at index 1
print(f"Removed: {removed_fruit}")  # cherry
print(fruits)  # ['pear', 'orange', 'grape', 'kiwi']

del fruits[0]                    # Delete element at index 0
print(fruits)  # ['orange', 'grape', 'kiwi']

fruits.clear()                   # Remove all elements
print(fruits)  # []