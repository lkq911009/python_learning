name = input("What is your name? ")
sale_amount = float(input("What is the sale amount? "))
print("Hello {}, your commission amount is {}".format(name, round(sale_amount * 13 / 100, 2 )))