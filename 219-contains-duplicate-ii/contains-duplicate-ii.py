class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
# creating a set to store the unique elements within the sliding window
        window = set()
# left pointer at the start for the sliding window
        l = 0
# iterate through the array with the right pointer
        for r in range(len(nums)):
# maintain the window size constraint by removing the leftmost element
            if r - l > k:
# remove the element that is out of the window range
                window.remove(nums[l])
# incrementally move the left pointer
                l += 1     
# if in the set, a duplicate exists withing the specified range (k)
            if nums[r] in window:
# return True early break out saves time
                return True
# add the current element to the set
            window.add(nums[r])
# no duplicates have been found, therefore return false
        return False