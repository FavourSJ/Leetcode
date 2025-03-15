class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()

        smallest = nums[0]
        largest = nums[-1]

        while largest:
            smallest, largest = largest, smallest % largest
        return smallest