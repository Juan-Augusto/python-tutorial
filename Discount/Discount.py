product_price = float(input("Enter the product price: "))
discount_percentage = float(input("Enter the discount percentage: "))
print("The new price is {}".format(product_price - (product_price * discount_percentage / 100)))