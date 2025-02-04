class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Converting the number to a string and check if it reads the same forwards and backwards
        return str(x) == str(x)[::-1]
        