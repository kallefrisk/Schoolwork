
def inc(n):
    n += 1
    return n


def inc_with(n, t):
    n = n + t
    return n


def greatest(n, m):
    return n if n > m else m


def is_even(n):
    return n % 2 == 0


def power(x, n):
    x = x ** n
    return x


def factorial(n):
    sum = n
    for i in range(1, n):
        sum = sum * i
    return sum


def is_prime(n):
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break
    return prime


print(f"One more than 50 is {inc(50)}")
print(f"63 plus 7 is {inc_with(63, 7)}")
print(f"Which is greater? 27 or 38?  The answer is {greatest(27, 38)}")
print(f"Is 9 even? {is_even(9)}")
print(f"49 to the power of 2 is {power(49, 2)}")
print(f"The factorial of 52 is {factorial(52)}")
print(f"Is 7719 prime? {is_prime(15)}")
