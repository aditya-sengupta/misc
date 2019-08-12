def add_as_str(s1, s2):
    """
    let's say we have '847' and '324'
    reverse them
    take s1[0] and s2[0] in strings
    add ints of both
    push result mod 10 to a new string (1) and set carry = 1
    then take s1[1] and s2[1]
    add ints of both plus carry
    push result mod 10 to the string (7) and set carry = 0
    then take s1[2] and s2[2]
    add ints of both plus carry
    push result mod 10 to the string (1) and set carry = 1
    oops we're at the end of our string
    so let's push carry to the string and return the reversed string
    """
    s1, s2, result, carry = s1[::-1], s2[::-1], "", 0
    if len(s1) > len(s2):
        s2 = s2 + '0'
    elif len(s2) > len(s1):
        s1 = s1 + '0'
    #now for every fib number, the two strings we're adding have the same length.
    for index in range(len(s1)):
        digitsum = sum([int(s1[index]), int(s2[index]), carry])
        result += str(digitsum%10)
        carry = digitsum // 10
    if carry:
        result += str(carry)
    return result[::-1]

k = 51
f_last = '12586269025'
f_before = '7778742049'
f_current = add_as_str(f_last, f_before)
while len(f_current) < 1000:
    f_before = f_last
    f_last = f_current
    f_current = add_as_str(f_last, f_before)
    k += 1
print(k)
