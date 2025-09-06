class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        l, r = 0, n - 1

        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            elif not s[r].isalnum():
                r -= 1
                continue
            elif s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
            
        return True