class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
########## Solution 1: Brute Force
        # n = len(nums)

        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[i] + nums[j] == target:
        #             return (i, j)
########## Solution 2: Maths
        prevmap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevmap:
                return [prevmap[diff], i]
            prevmap[n] = i