class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        prefix_sum = 0
        min_start_value = 1

        for n in nums:
            prefix_sum += n
            min_start_value = max(min_start_value, 1 - prefix_sum)
        return min_start_value