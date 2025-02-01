# 2 pointers solution
# linear  time solution O(n)
# no extra memory is needed O(1)

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        l = 0 # implementing a slider from the beginning
        product = 1

        for r in range(len(nums)):
            product *= nums[r]
# (edge case) ensures the left pointer does not past the right pointer AND not greater than k
            while l <= r and product >= k: 
                product = product // nums[l]
                l += 1

            res += (r - l + 1)

        return res
        