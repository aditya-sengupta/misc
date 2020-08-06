import tqdm
highest = 1000000

counts = [0] * highest
counts[1] = 1

def collatz(x):
    if x % 2 == 0:
        return x // 2
    return 3 * x + 1

def chain_length_uncached(x):
    if x == 1:
        return 1
    return chain_length_uncached(collatz(x)) + 1

def count_chain_length(x):
    c = collatz(x)
    if x == 1:
        return 1
    if c < highest and counts[c] != 0:
        counts[x] = counts[c] + 1
    elif c < highest:
        counts[x] = count_chain_length(c) + 1
    else:
        return chain_length_uncached(c) + 1
    return counts[x]

for i in tqdm.trange(1, highest):
    count_chain_length(i)

print(counts.index(max(counts)))
