# Sliding window problem
# 2 pointer solution left and right, then iterate through, and have a counter
# we will use a hashmap because, as there will be multiple copies of a given value

# sliding window with 3 pointers
# time complexity of O(n)
# due to the hashmap the space complexity is O(n)

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        res = 0
        l_far = 0 #left pointer far
        l_near = 0 # left pointer near

        for r in range(len(nums)):
            count[nums[r]] += 1

# while loops to decide when to shift the pointers
            while len(count) > k:
                count[nums[l_near]] -= 1
                if count[nums[l_near]] == 0:
                    count.pop(nums[l_near])
                l_near += 1
                l_far = l_near

            while count[nums[l_near]] > 1:
                count[nums[l_near]] -= 1
                l_near += 1

            if len(count) == k:
                res += l_near - l_far + 1


        return res
        