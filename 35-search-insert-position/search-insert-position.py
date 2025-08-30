class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if target <= num:
                return i  # target found or should be inserted here
        return len(nums)
