class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[n] == 0:
                nums[n], nums[fast] = nums[fast], nums[n]

            if nums[n] != 0:
                n += 1

        