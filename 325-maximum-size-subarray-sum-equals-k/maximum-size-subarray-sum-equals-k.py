class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum = 0 # Keeps track of the cumulative sum
        max_length = 0 # Stores the maximum length of a subarray summing to k
        prefix_map = {0: -1} # Hashmap to store first occurrence of a prefix sum

        for i, num in enumerate(nums): # Loop through the array
            prefix_sum += num # Update cumulative sum

            # Check if there exists a subarray that sums to k
            if prefix_sum - k in prefix_map:
                max_length = max(max_length, i - prefix_map[prefix_sum - k])

            # Store the first occurrence of this prefix sum
            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum] = i
        
        return max_length
        