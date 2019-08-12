"""If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage."""

digit = lambda x, place: (x - (x%place))/place

def lettercount(number):
    if(number == 1000):
        return 11
    elif(number > 100):
        hundreds = digit(number, 100)
        if(lettercount(number - 100*hundreds)==0):
            return lettercount(hundreds) + 7
        return lettercount(hundreds) + lettercount(number - 100*hundreds) + 10
    elif(number == 100):
        return 10
    elif(number > 19):
        tens = digit(number, 10)
        if(tens in [2, 3, 8]):
            return lettercount(number - 10*tens) + 6
        elif(tens==7):
            return lettercount(number - 10*tens) + 7
        else:
            return lettercount(number - 10*tens) + 5
    elif(number in [1, 2, 6, 10]):
        return 3
    elif(number in [3, 7, 8]):
        return 5
    elif(number in [4, 5, 9]):
        return 4
    elif(number in [11, 12]):
        return 6
    elif(number in [15, 16]):
        return 7
    elif(number==17):
        return 9
    elif(number in [13, 14, 18, 19]):
        return 8
    else:
        return 0

sum = 0
for i in range(1, 1001):
    sum += lettercount(i)
print(sum)

"""
pseudocode
if number is 1000:
    add 11

if first digit is in the hundreds:
    add regular letter count corresponding to that number
    add 7 for "hundred"
    if next two are not zeros:
        add 3 for "and"
        go to procedure for dealing with two digit numbers

if first digit is in the tens and >=2:
    add numbers corresponding to 20-90
    go to procedure for dealing with 1-19

if 1-19:
    add manually

    one, two, six, ten - 3
    three, seven, eight - 5
    four, five, nine - 4
    eleven, twelve - 6
    fifteen, sixteen - 7
    thirteen, fourteen, eighteen, nineteen - 8
    seventeen - 9
"""
