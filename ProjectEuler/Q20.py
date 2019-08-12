def fact(n):
    if n < 2:
        return 1
    return n * fact(n - 1)

def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)

print(sum_digits(fact(100)))

#this isn't really in the spirit of the question lol
