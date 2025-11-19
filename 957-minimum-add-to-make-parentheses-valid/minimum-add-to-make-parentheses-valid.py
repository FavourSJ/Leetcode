class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openP = 0
        closedP = 0

        for c in s:
            if c == '(':
                openP += 1
            elif c == ')' and openP > 0:
                openP -= 1
            else:
                closedP += 1
        
        return openP + closedP