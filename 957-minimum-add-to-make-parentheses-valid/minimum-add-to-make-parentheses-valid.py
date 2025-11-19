class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        additions = 0

        for ch in s:
            if ch == "(":
                balance += 1
            else:  # ch == ")"
                if balance > 0:
                    balance -= 1
                else:
                    additions += 1  # need to insert a "("

        # For any unmatched "(" left, we need to insert ")"
        additions += balance

        return additions