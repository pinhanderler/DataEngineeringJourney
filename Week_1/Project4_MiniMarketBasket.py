# Project 4: Mini Market Basket 

products = {"apple": 3, "banana": 5, "bread": 2, "milk": 4}

print("Available products:", list(products.keys()))

basket = []
total = 0

for i in range(3):
    item = input(f"Enter product {i+1}: ").lower()
    if item in products:
        basket.append(item)
        total += products[item]
    else:
        print(f"⚠️ '{item}' not found in market.")

print("\nYour basket:", ", ".join(basket))
print("Total price:", total, "TL")
