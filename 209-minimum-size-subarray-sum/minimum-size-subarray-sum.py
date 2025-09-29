class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        summ = 0
        l = 0

        for r in range(len(nums)):
            summ += nums[r]

            while summ >= target:
                min_length = min(min_length, r - l + 1)
                summ -= nums[l]
                l += 1

        if min_length < float('inf'):
            return min_length
        else:
            return 0