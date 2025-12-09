
n = int(input("n="))
m = int(input("m="))

if m < n:
    print(f"{n} is greater than {m}")
elif m == n:
    print(f"{n} is equal to {m}")
else:
    print(m, "is greater than", n)


