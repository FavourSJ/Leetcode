class Solution:
    def singleNumber(self, nums: List[int]) -> int:
# creating the result
        res = 0
# iterate through the array
        for n in nums:
# using the xor operation which returns a duplicate already
            res = n ^ res
        return res