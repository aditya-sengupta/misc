import tqdm

highest = 28123

def d(n):
    total = 0
    for divisor in range(1, n//2 + 1):
        if n % divisor == 0:
            total += divisor
    return total

abundant = []
for i in tqdm.trange(highest):
    if d(i) > i:
        abundant.append(i)

reachables = set()
for i in tqdm.tqdm(abundant):
    for j in abundant:
        reachables.add(i + j)

allnums = set(range(highest))
unreachables = allnums - reachables
print(sum(unreachables))
