def reversed_string(a_string):
    return a_string[::-1]

def double_from_string(num_str):
    doubled_string = ''
    carry = 0
    num_str = reversed_string(num_str)
    for i in num_str:
        digit = 2*int(i) + carry
        carry = int((digit - (digit%10))/10)
        doubled_string += str(int(digit%10))
    if(carry == 1):
        doubled_string += '1'
    return reversed_string(doubled_string)

s = '1'
sum = 0
for _ in range(1000):
    s = double_from_string(s)
for digit in s:
    sum += int(digit)
print(sum)
