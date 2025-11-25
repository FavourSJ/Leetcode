# sliding window approach
# Time Complexity O(N)
# Space Complexity O(N)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        charcount = set()
        n = len(s)

        for r in range(n):
            # if duplicate character is found we will move left up by 1
            while s[r] in charcount:
                charcount.remove(s[l])
                l += 1

            # find size of current window size
            window = (r - l) + 1
            longest = max(longest, window)
            
            # add a new character to the set
            charcount.add(s[r])

        return longest