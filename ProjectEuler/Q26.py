"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

"""
The test for recurrence: multiply by 10, see time till you get the same thing you started with on the right.
for i in range(1000)
start frac = float(1/i)
make a list of fractions w/ frac as the first element
multiple times: frac *= 10, frac -= frac//1, push to list. break if you ever get 0
if you ever get an element that's in the list, check the distance from that element and there's your answer

frac = float(1/7) = 0.142857...
fraclist = [frac]
frac *= 10
frac -= frac//1
fraclist.append(frac)
fraclist = [0.142857..., 0.42857...]
frac *= 10
frac -= frac//1
fraclist.append(frac)
fraclist = [0.142857..., 0.428571..., 0.285714...]
"""

def approx_eq(x, y, tolerance=1e-10):
    return abs(x - y) < tolerance

def recurring_cycle(n):
    frac = float(1/n)
    fraclist = []
    while frac:
        fraclist += [frac]
        frac *= 10
        frac -= frac//1
        for index, element in enumerate(fraclist):
            if approx_eq(frac, element):
                return len(fraclist) - index
    return 0

"""
ok this is ugly because it involves float comparisons. Let me try and think up a different way of doing things.
"""

def recurring_cycle(n):
    remainders = []
    multiplier = 10**len(str(n))
    r = multiplier % n
    while r and r not in remainders:
        remainders += [r]
        r = (multiplier * r) % n
    if not r:
        return 0
    for index, element in enumerate(remainders):
        if r == element:
            return len(remainders) - index

def main():
    max_recur, max_index = 1, 3
    for i in range(3, 1000):
        r = recurring_cycle(i)
        if r > max_recur:
            max_index = i
            max_recur = r
    return max_index

print(main())
