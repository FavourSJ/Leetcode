class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
# creating a set to store values
        hashset = set()

# iterate through the array
        for n in nums:
# check to see value is already in hashset
            if n in hashset:
# if so -> TRUE
                return True
# if not add to hashset and carry on
            hashset.add(n)
# no duplicates -> FALSE
        return False