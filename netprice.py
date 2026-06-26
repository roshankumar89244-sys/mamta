# discount and net price
price = float(input("Enter price: "))
discount = float(input("Enter discount percentage: "))
discount_amount = (discount / 100) * price
net_price = price - discount_amount
print("Discount amount is:", discount_amount)
print("Net price is:", net_price)
