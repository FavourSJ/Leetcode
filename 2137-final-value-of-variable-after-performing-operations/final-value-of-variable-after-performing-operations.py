class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0

        for i in operations:
            if i == "++X" or i == "X++":
                res += 1
            elif i == "--X" or i == "X--":
                res -= 1
        return res