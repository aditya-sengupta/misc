def d(n):
    total = 0
    for divisor in range(1, n//2 + 1):
        if n % divisor == 0:
            total += divisor
    return total

total = 0
i = 0
for i in range(10000):
    if d(d(i)) == i and i != d(i):
        total += i
print(total)
