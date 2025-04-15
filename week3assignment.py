#Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. 
# The function should take the original price (price) and the discount percentage (discount_percent) as parameters. 
# If the discount is 20% or higher, apply the discount; otherwise, return the original price.
def calculate_discount(price, discount_percent):
    final_price=float(price * ((100-discount_percent)/100))
    if discount_percent > 20:
        return f"Final price of product is: {final_price}"
    else:
        return f"No discount, price is: {price}"
print(calculate_discount(33000.55,21.15))
#Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. 
# Print the final price after applying the discount, or if no discount was applied, print the original price.
def calculate_discount():
    price=float(input("Enter price of item: "))
    discount_percent=float(input("Enter the discount: "))
    final_price=price * ((100-discount_percent)/100)
    if discount_percent == 0:
        return f"Since no discount, price is: {price}"
    else:
        return f"Final price is: {float(final_price)}"
    
print(calculate_discount())