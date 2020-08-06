from scipy.special import factorial
from functools import partial, reduce

def naive_method():
    map_and_sum = lambda n, fn: int(sum([fn(int(i)) for i in str(n)]))
    direct_sum = partial(map_and_sum, fn=lambda x: x)
    f = partial(map_and_sum, fn=factorial)
    sf = lambda n: direct_sum(f(n))

    g = {}
    hits = set(range(1, 151))
    j = 1
    while hits:
        try:
            if j % 1000 == 0:
                print(min(hits), sum(map(direct_sum, g.values())))
            val = sf(j)
            if val in hits:
                hits.remove(val)
                g[val] = j
            j += 1
        except KeyboardInterrupt:
            print(g)
            raise

    print(sum(map(direct_sum, g.values())))

naive_method()
