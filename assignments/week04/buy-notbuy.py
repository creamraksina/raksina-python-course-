budget = 0
total = 0

print("-"*40)
print("                 Budget")
print("-"*40)
print()
  
prices = []
bought_item = []

print("Enter prices of 6 item :")
for i in range(6):
    price_item = int(input(f"Item {i+1}: "))
    prices.append(price_item)

print()

budget = int(input("Enter your budget: "))

print()

for i in range(6):
    if total + prices[i] <= budget:
        print(f"Item {i+1}: prince {prices[i]} | Can buy.")
        bought_item.append(prices[i])
        total = total + prices[i]
        print(f"Current total = {total}")
        
    else:
        print(f"Item {i+1}: prince {prices[i]} | Can't buy.")
        print(f"Current total = {total}")
   
    
print()
                
print(f"Bought item : {bought_item}")
print(f"Total spent : {total}")
print(f"Remining budget : {budget - total}")
    


