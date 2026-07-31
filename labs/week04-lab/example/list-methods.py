# Sample data
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
fruits = ["apple", "banana", "apple", "orange"]

# Length and counting
print(f"Length: {len(numbers)}")           # 9 ถามหาจำนวนสามาชิกที่อยู่ในลิส  len
print(f"Count of 1: {numbers.count(1)}")   # 2 การถามว่าในตัวแปรชื่อ numbers มี 1 อยู่กี่ตัว ถ้าเป็น 0 คือไม่มี
print(f"Count of apple: {fruits.count('apple')}")  # 2 count การนับจำนวนของตัวที่เราอยากนับ

# Finding elements
print(f"Index of 4: {numbers.index(4)}")   # 2 ถามว่า 4 อยู่ใน index อะไร
print(f"Index of banana: {fruits.index('banana')}")  # 1 หาว่า banana อยู่ในตำแหน่ง index อะไร

# Sorting
numbers_copy = numbers.copy()   #  copy การทำสำเนาลิส 
numbers_copy.sort()   #เรียงจากน้อยไปหามาก         # Sort in place
print(f"Sorted: {numbers_copy}")           # [1, 1, 2, 3, 4, 5, 5, 6, 9]

numbers_copy.sort(reverse=True) #เรียงจากมากไปหาน้อย            # Sort descending
print(f"Reverse sorted: {numbers_copy}")   # [9, 6, 5, 5, 4, 3, 2, 1, 1]

# sorted() function - returns new list
sorted_numbers = sorted(numbers) #ต้องมีตัวแปรมารับเสมอ
print(f"Original: {numbers}")              # [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(f"New sorted: {sorted_numbers}")     # [1, 1, 2, 3, 4, 5, 5, 6, 9]

# Reversing
fruits.reverse() #ข้อมูลที่อยู่ในลิสจะกลับด้าน หลังมาหน้า 
print(f"Reversed fruits: {fruits}")        # ['orange', 'apple', 'banana', 'apple']

# Min, max, sum (for numeric lists)
print(f"Min: {min(numbers)}")              # 1 หาค่าน้อยสุดในลิส
print(f"Max: {max(numbers)}")              # 9 หาค่ามากสุดในลิส
print(f"Sum: {sum(numbers)}")              # 36 หาผลรวมในลิส


#แล้วการหาค่าเฉลี่ย numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
averange = sum(numbers)/ len(numbers)
