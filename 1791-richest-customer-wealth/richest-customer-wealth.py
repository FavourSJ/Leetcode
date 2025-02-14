class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealthSoFar = 0

        for i in range(len(accounts)):
            totalWealth = sum(accounts[i])
            maxWealthSoFar = max(maxWealthSoFar, totalWealth)
            
        return maxWealthSoFar


        