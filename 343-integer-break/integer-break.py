class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        
        q = n // 3
        r = n % 3
        
        if r == 0:
            return 3 ** q
        elif r == 1:
            return 3 ** (q - 1) * 4
        else:  # r == 2
            return 3 ** q * 2