print('Hi, welcome to some place')
price_1 = float(input('Price of the first item $'))
price_2 = float(input('Price of the second item $'))
member = int(input('Enter 1 if you are a member and 0 if you arent a memeber: '))
tax_amount = float(.0825 *(price_1 + price_2))
member_discount = float((price_1 + price_2) * .10)
if (member == 1):
    cost = price_1 + price_2 + tax_amount - member_discount
    print("Your total cost is", cost)
elif (member == 0):
      cost = price_1 + price_2 + tax_amount
      print("Your total cost is", cost)
else:
    print('Invalid entry')


