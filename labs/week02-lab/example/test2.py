print("2. Time Converter:")
print("   - Ask user for seconds")
print("   - Convert to hours, minutes, and remaining seconds")
print("   - Example: 3661 seconds = 1 hour, 1 minute, 1 second")
print("_"*50)
print()

#input
seconds = int(input("Input second : "))

#processs
hour = seconds // 3600
seconds_remain = seconds % 3600
minute = seconds_remain // 60
second_remain = minute * 60

#output
print(f"{seconds} = seconds = {hour} hour(s), {minute} minute(s) ,{second_remain} second(s)")