class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        # Calculate the sum of elements in nums1 and the number of zeros
        sum1 = sum(nums1)
        zeros1 = nums1.count(0)

        # Calculate the sum of elements in nums2 and the number of zeros
        sum2 = sum(nums2)
        zeros2 = nums2.count(0)

        # Calculate the minimum possible sum for each array after replacing zeros with 1s
        min_sum1 = sum1 + zeros1
        min_sum2 = sum2 + zeros2

        # If it's impossible to make the sums equal
        if (zeros1 == 0 and sum1 < sum2 + zeros2) or (zeros2 == 0 and sum2 < sum1 + zeros1):
            return -1

        # Return the minimum equal sum we can obtain
        return max(min_sum1, min_sum2)