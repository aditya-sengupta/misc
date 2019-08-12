from math import sqrt

def isprime(test, L):
  for prime in L:
    if (test%prime)==0:
        return False
    if prime > int(sqrt(test)):
        return True

def make_prime_list(max_int, prime_list = [2]):
    max_prime = max(prime_list)
    for i in range(max_prime+1, max_int):
        if isprime(i, prime_list):
            prime_list.append(i)
    return prime_list

def num_factors(N):
    factors = 1
    for prime in make_prime_list(int(N/2)):
        prime_exp = 0
        while(N%prime==0):
            N /= prime
            prime_exp+=1
        factors *= (prime_exp+1)
        if N == 1:
            break
    return factors


triangle, inc = 28, 8
while True:
    triangle += inc
    if num_factors(triangle) > 500:
        print(triangle)
        break
    inc += 1
