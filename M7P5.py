sumDiscounts = 0
print("Do you want to continue? Yes or No")
response = input()
while response == "Yes":
    print("Enter quantity")
    quantity = int(input())
    print("Enter price")
    price = float(input())
    extendedPrice = quantity * price
    if extendedPrice > 10000:
        discountPercent = 0.25
    else:
        discountPercent = 0.1
    discountAmount = extendedPrice * discountPercent
    total = extendedPrice - discountAmount
    print("Extended Price:")
    print(extendedPrice)
    print("Discount amount:")
    print(discountAmount)
    print("Total:")
    print(total)
    sumDiscounts = sumDiscounts + discountAmount
    print("Would you like to add another order? Yes or No")
    response = input()
print("Sum of all discounts:")
print(sumDiscounts)
