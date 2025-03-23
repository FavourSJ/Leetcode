class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
# keeps track of the cumulative sum at each index
        prefix_sum = 0
# stores the maximum length of a subarray summing to k
        max_length = 0
# hashmap to store the first occurence of a prefix sum
# will do it {0: -1} to handle cases where a prefix sums itself equals k
        prefix_map = {0: -1}

# loop through the array
        for i, num in enumerate(nums):
            prefix_sum += num

# check if there exists a subarray ending at index i that sums to keeps
# this means checking if (prefix_sum - k) has been seen before
            if prefix_sum - k in prefix_map:
# if found -> calculate the length of this subarray and update the max_length
                max_length = max(max_length, i - prefix_map[prefix_sum - k])

# store the first occurence of this prefix sum
# we only store the first occurence as we want the longest subarray
            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum] = i

        return max_length