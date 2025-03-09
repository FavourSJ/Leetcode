# hard part is not using any memory

# Time complexity
# Space complexity

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0 # creating the result

        for n in nums:
            res = n ^ res # xor the code so that if the number is the same it wont return it
        return res
        