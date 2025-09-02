class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closets = nums[0]

        for num in nums:
            if abs(num) < abs(closets):
                closets = num

        if closets < 0 and abs(closets) in nums:
            return abs(closets)
        else:
            return closets