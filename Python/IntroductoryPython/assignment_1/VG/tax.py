inc = int(input("Please provide monthly income: "))                                 # Input salary

statement = "Your corresponding income tax:"

if inc > 0:                                                                         # Check if positive
    if inc < 38000:
        sum = round(0.3*inc)
        print(statement,sum)
    elif 38000 <= inc < 50000:                                                      # Compute depending on income level and print
        sum = round(0.3*inc + (inc - 38000)*0.05)
        print(statement,sum,)
    else:
        sum = round(0.3*inc + (inc - 50000)*0.05 + (inc - 38000)*0.05)
        print(statement,sum)
else:
    print("Income needs to be positive!")
