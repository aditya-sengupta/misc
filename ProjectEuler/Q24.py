"""A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"""

"""
let's try and solve a simpler problem first: 20th permutation of 0, 1, 2, 3
because for that I can write out the entire algorithm run
so we call a certain function that I haven't yet named on inputs (20, range(4))
so there's a total of fact(4) = 24 permutations
I'm going to fix 0 at the start
There's a total of fact(3) = 6 permutations with this fixed
6 < 20 so let's fix 0 + 1 = 1 at the start
There's a total of fact(3) = 6 permutations with this fixed
12 < 20 so let's fix 1 + 1 = 2 at the start
There's a total of fact(3) = 6 permutations with this fixed
18 < 20 so let's fix 2 + 1 = 3 at the start
There's a total of fact(3) = 6 permutations with this fixed
24 > 20 so 3 at the start is correct
so let's delete 3 from our list that started as [x for x in range(4)]
numlist.remove(3)
now let's run this algorithm on inputs (20 - 18 = 2, numlist)
we want to find the second permutation of [0, 1, 2] now
I'm going to fix 0 at the start
there's a total of fact(2) = 2 permutations with this fixed
2 = 2 so 0 at the start is correct
I'm going to fix 1 at the start
there's a total of fact(1) = 1 permutations with this fixed
And here's our base case, where I add 2 at the end.
out - 3012.
"""

def fact(n):
    if n < 2:
        return 1
    return n * fact(n - 1)

def permutation(n, use):
    #Return the Nth permutation of the digits of USE, assuming USE is a list of elements in order.
    pcount = 1
    for fixed in use:
        #there's fact(n - 1) permutations in this
        if pcount >= n:
            use.remove(fixed)
            return str(fixed) + permutation()
        else:
            fixed += 1
            pcount += fact(len(use) - 1)
