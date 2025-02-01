# DFS (Depth First Search)- Backtracking solution
# Start from the answer you are trying to get, and take away the different option
# Store sub problems in cache, to store answers, to reduce compute time
# Bottom-up solution

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1) # 0 ....... amount
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
# Reccurence relation: equation that recursively defines a sequence, where the next term is a function of the previous terms
                    dp[a] = min(dp[a], 1 + dp[a - c]) # recurrence relation
        return dp[amount] if dp[amount] != amount + 1 else -1

# time complexity = O(amount * len(coints))
# memory complexity = O(amount)