class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        l = 0
        r = len(nums) - 1

        res = set()

        while l < r:
            if nums[l] == nums[l + 1]:
                res.add(nums[l])
            if nums[r] == nums[r - 1]:
                res.add(nums[r])
            l += 1
            r -= 1

        return list(res)