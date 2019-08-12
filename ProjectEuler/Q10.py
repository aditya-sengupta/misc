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

def sum_primes(max_int):
    sum = 0
    for prime in make_prime_list(max_int):
        sum += prime
    return sum

print(sum_primes(int(2e6)))
