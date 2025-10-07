print("Mini Market Basket (Type 'exit' to finish)\n")

products = {"apple": 3, "banana": 5, "bread": 2, "milk": 4}

basket = []
total = 0

while True:
    item = input("Add product: ").lower()
    if item == "exit":
        break
    elif item in products:
        basket.append(item)
        total += products[item]
        print(f" {item} added ({products[item]} TL)")
    else:
        print(f" '{item}' not found in the market!")

print("\n Your basket:", ", ".join(basket))
print(f"Total price: {total} TL")
