class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set(nums1)
        
        ans = []
        seen2 = set()
        for num in nums2: 
            if num in seen and (num not in seen2):
                ans.append(num)
            seen2.add(num)
        
        return ans