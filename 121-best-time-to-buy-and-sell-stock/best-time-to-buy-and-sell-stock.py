# memory space O(1)
# Time O(n), scan through the array once - linear

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 # buying
        r = 1 # selling
        maxP = 0

        while r < len(prices):
            #profitable
            if prices[l] < prices[r]: # checking if buying is less than selling
                profit = prices[r] - prices[l] # calculation for profit
                maxP = max(maxP, profit) # store maximum profit
            else:
                l = r # shift the left pointer all the way to the lowest point
            r += 1 # keep on checking the sell price of the next point
        return maxP # return max profit
        