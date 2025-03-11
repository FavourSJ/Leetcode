# Time Complexity O(n logk)

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0:
            return False # Absolute difference can't be negative
        
        bucket_map = {} # Dictionary to store numbers in buckets
        bucket_size = valueDiff + 1 # Each bucket represents a range of `valueDiff`

        for i, num in enumerate(nums):
            bucket_id = num // bucket_size # assig number to its bucket

            # check if current bucket has a duplicate
            if bucket_id in bucket_map:
                return True
            
            # check neighbouring buckets for a valid pair
            if bucket_id - 1 in bucket_map and abs(num - bucket_map[bucket_id - 1]) <= valueDiff:
                return True
            if bucket_id + 1 in bucket_map and abs(num - bucket_map[bucket_id + 1]) <= valueDiff:
                return True

            # add current numbe to its bucket
            bucket_map[bucket_id] = num

            # maintain the sliding window size by removing old elements
            if i >= indexDiff:
                del bucket_map[nums[i - indexDiff] // bucket_size]
        
        return False # no valid pair found

        