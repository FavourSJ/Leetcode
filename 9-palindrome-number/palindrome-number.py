class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending with 0 (except 0 itself) can't be palindromes
        if x < 0:
            return False
        
        # Converting the number to a string and check if it reads the same forwards and backwards
        return str(x) == str(x)[::-1]
        