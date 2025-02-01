# sliding window solution
# time complexity of O(n) as it is linear

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
# creation of the max value, at first it will be the first value in the array
# can't be zero as there are negative values
        maxSub = nums[0]
        curSum = 0 # this will hold the current value

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub

        