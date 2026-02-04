class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Initialize the smallest value and middle value to infinity
        smallest = float('inf')
        middle = float('inf')
        # These represent the first two elements of a potential triplet

        # Iterate through each number in the array
        for current_num in nums:
            # if we find a number greater than middle, we have found our triplet
            if current_num > middle:
                return True
                # This means we have: smallest < middle < current_num
            # If current number is less than or equal to smallest, update smallest
            elif current_num <= smallest:
                smallest = current_num
                # This ensures we always track the minimum value seen so far
            # If current number is greater than smallest but not greater than middle, update middle to current number
            else:
                middle = current_num
                # This means we found a valid pair (smallest, current_num)
        # No increasing triplet was found after scanning the entire array
        return False

        # T: O(n)
        # S: O(1)