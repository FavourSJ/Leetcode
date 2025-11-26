class Solution:
    def isUgly(self, n: int) -> bool:
        # ugly numbers must be positive
        if n <= 0:
            return False

        # repeatedly divide n by the allowed prime factors which is 2,3 and 5
        for prime in [2, 3, 5]:
            # while n is divisible by this prime, keep dividing it, then move to the next
            while n % prime == 0:
                n = n // prime

        # n must be reduced to 1 to be considered ugly
        if n == 1:
            return True

        return False