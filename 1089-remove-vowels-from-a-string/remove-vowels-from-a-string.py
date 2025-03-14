class Solution:
    def removeVowels(self, s: str) -> str:
        res = []
	
        for i in range(len(s)):
            if s[i] not in 'aeiou':
                res.append(s[i])
        
        return ''.join(res)