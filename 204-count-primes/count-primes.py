# Sieve of Eratosthenes Algorithm

class Solution:
    def countPrimes(self, n: int) -> int:
        # if n is less than 2 there are no primes at all
        if n < 2:
            return 0

        # create a boolean list where is_prime[i] indicates if i is prime or not
        # assume every number is prime
        is_prime = [True] * n
        # 0 and 1 are not prime
        is_prime[0] = is_prime[1] = False

        # start from i = 2
        i = 2
        # iterate up until the square root of n becase any composite < n must have a factor
        while i * i < n:
            # if i is still marked prime, mark all its multiples as not prime then
            if is_prime[i]:
                # marking from i*i, as smaller multiples were already handled
                for j in range(i * i, n, i):
                    is_prime[j] = False

            i += 1
        
        return sum(is_prime)
        