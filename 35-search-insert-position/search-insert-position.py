class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        while l <= r:
            middle = (l + r) // 2
            if nums[middle] < target:
                l = middle + 1
            elif nums[middle] > target:
                r = middle - 1
            elif nums[middle] == target:
                return middle
        
        if nums[middle] < target:
            return middle + 1
        else:
            return middle


# Brute Force approach
        # for i, num in enumerate(nums):
        #     if target <= num:
        #         return i  # target found or should be inserted here
        # return len(nums)