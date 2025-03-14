class Solution:
    def orArray(self, nums: List[int]) -> List[int]:
        return [nums[n] | nums[n - 1] for n in range(1, len(nums))]
