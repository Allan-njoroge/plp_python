def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (price * (discount_percent/100))
    
    else:
        return price
    
original_price = float(input("Price: "))
percentage = float(input("Discount: "))

final_price = calculate_discount(original_price, percentage)

print(f"Final Price: ${final_price}")