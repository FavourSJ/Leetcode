class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set()
        result = set()

        for x in nums1:
            seen.add(x)        # track unique from nums1

        for x in nums2:
            if x in seen:
                result.add(x)  # add to result only once
        return list(result)