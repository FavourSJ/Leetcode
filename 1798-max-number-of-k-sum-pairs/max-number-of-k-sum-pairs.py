class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        ans = 0

        while left < right:
            total = nums[left] + nums[right]

            if total == k:
                ans += 1
                left += 1
                right -= 1
            elif total > k:
                right -= 1
            elif total < k:
                left += 1

        return ans

        # T: O(nlog n)
        # S: O(log n)