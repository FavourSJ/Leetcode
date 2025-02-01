# brute force backtracking problem
# time complexity O(n.4^n)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        # creation of a hashmap for all of the characters
        digit_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        # backtracking function
        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            for c in digit_letters[digits[i]]:
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")

        return res   