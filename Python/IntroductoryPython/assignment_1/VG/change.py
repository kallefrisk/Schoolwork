# Input price and payment
price = float(input("price: "))

payment = float(input("payment: "))

# Calculate change and round it
change = round(payment - price)

# Compute the amount of bills with integer-division and use modular division to se what remains
b1000 = change//1000
b1000res = change % 1000

# Repeat this step for all bills and coins
b500 = b1000res//500
b500res = b1000res % 500

b200 = b500res//200
b200res = b500res % 200

b100 = b200res//100
b100res = b200res % 100

b50 = b100res//50
b50res = b100res % 50

b20 = b50res//20
b20res = b50res % 20

c10 = b20res//10
c10res = b20res % 10

c5 = c10res//5
c5res = c10res % 5

c2 = c5res//2
c2res = c5res % 2

c1 = c2res//1

# Present results
print("Your change amounts to:", change, "kr")
print("1000kr bills: ", b1000)
print("500kr bills: ", b500)
print("200kr bills: ", b200)
print("100kr bills: ", b100)
print("50kr bills: ", b50)
print("20kr bills: ", b20)
print("10kr coins: ", c10)
print("5kr coins: ", c5)
print("2kr coins: ", c2)
print("1kr coins: ", c1)