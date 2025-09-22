class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        while l < r:
            middle = (l + r) // 2

            if nums[middle] > nums[r]:
                l = middle + 1
            else:
                r = middle

        return nums[l]
        