class Solution:
    def reverseVowels(self, s: str) -> str:
        l = len(s)
        vowels = [i for i in range(l) if s[i] in ['a','e','i','o','u','A','E','I','O','U']][::-1]
        co = 0
        ls = list(s)
        for c in s:
            if c in ['a','e','i','o','u','A','E','I','O','U']:
                ls[vowels[co]] = c
                co += 1
        return ''.join(ls)
        