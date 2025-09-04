class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (sorted(s) != sorted(t)) or (len(s) != len(t)):
            return False
        else:
            return True
        