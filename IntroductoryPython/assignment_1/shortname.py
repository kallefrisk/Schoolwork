fi = str(input("First name: "))
mi = str(input("Middle name: "))                                # Input Names
la = str(input("Last name: "))

n1 = fi[0]

n2 = mi[0]                                                      # Convert names into short version

n3 = la[0:4]

print(n1, ". ", n2, ". ", n3, sep="")                               # Print results
