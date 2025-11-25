class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # count for open brackets
        openB = 0
        #count for closed brackers
        closedB = 0

        for ch in s:
            if ch == "(":
                # confiremd open bracket
                openB += 1
                # we have found a match so no need to add an open bracket here
            elif ch == ")" and openB > 0:
                openB -= 1
            else:
                # no open bracket to match what we need
                closedB += 1

        return openB + closedB
