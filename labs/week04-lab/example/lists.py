# Empty list
empty_list = [] #สร้าง list เปล่าหรือว่าง ต้องใช้เครื่องหมาย[]
another_empty_list = list() # ไม่ก็เรียกใช้ฟังก์ชั่น list()

# List with initial values
fruits = ["apple", "banana", "orange"] #เจอ[]บ่งบอกถึงการเป็นลิส ลิสเป็น str
numbers = [1, 2, 3, 4, 5] # ลิสเก็บ int
mixed_list = [1, "hello", 3.14, True] #list สามารถผสมได้ in Python

# in C Array = int number[]={1,2,3,4,5,};

# List from range
numbers_range = list(range(1, 11))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #สร้าง range ที่มีขนาดช่วงตั้งแต่ 1 ถึง 11-1

# List from string
letters = list("hello")  # ['h', 'e', 'l', 'l', 'o'] #การระเบิดคำเป็นทีละตัว เนื่องจากคำสั่ง letters

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Mixed: {mixed_list}")