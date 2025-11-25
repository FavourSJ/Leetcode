# memory space O(1)
# Time O(n), scan through the array once - linear

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # pointer for the left
        l = 0
        # pointer for the right 1 position ahead
        r = 1
        # create a place to store the max profit
        maxP = 0

        # while loop to iterate through the array as long as there are values
        while r < len(prices):
            #if the price before is less than the prices after...
            if prices[l] < prices[r]:
                # calculate the profit and store the result
                profit = prices[r] - prices[l]
                # compare this value to the max profit
                maxP = max(maxP, profit)
        # if it is not greater than the previous maxprofit...
            else:
                # shift the left pointer to the new "lowest position" r will automatically go there
                l = r
        #then keep iterating through
            r += 1

        # return this final max profit
        return maxP
        