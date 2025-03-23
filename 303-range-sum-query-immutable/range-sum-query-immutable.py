class NumArray:

    def __init__(self, nums: List[int]):
# a store for the cumulative sum of each index
        self.prefix = []
# a store for the running sum
        cur = 0

# constructing the prefix sum array
        for n in nums:
            cur += n
            self.prefix.append(cur)

    def sumRange(self, left: int, right: int) -> int:
# sum of elements from index 0 to right
        rightSum = self.prefix[right]

# if left is greater than 0, subtract the sum up to (left - 1)
# to get the range sum
        if left > 0:
            leftSum = self.prefix[left - 1]
        else:
# if left is zero no need to subtract anything
            leftSum = 0

# return the calculation in the given range
        return rightSum - leftSum



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)