class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        if n == 0:
            return 0
        k = int(math.log(n, 5))  # largest power of 5 <= n
        for i in range(1, k + 1):
            count += n // (5 ** i)
        return count
        