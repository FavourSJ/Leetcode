class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        first = list(set(nums1) - set(nums2))
        second = list(set(nums2) - set(nums1))
        return [first, second]
        