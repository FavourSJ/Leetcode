# dynamic programming solution
# time complexity is O(n*n) better than brute force which has a time complexity of O(2^n)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums) # cache list initally set to one, with a length of the input array

        # this starts at the last array and moves through to the beginning
        for i in range(len(nums) - 1, -1, -1):
            # starts at the beginning and moves untill the end
            for j in range(i + 1, len(nums)):
                # condition to ensure that the number after is less than the one before
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)

        