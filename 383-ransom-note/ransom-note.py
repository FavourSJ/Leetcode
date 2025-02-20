class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        x = Counter(ransomNote)
        y = Counter(magazine)

        if x & y == x:
            return True
        return False

        