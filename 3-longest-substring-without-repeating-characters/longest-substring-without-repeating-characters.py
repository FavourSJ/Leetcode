class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()  # Tracks unique characters in current window
        l = 0             # Left pointer of the window
        max_len = 0       # Stores max length found

        for r in range(len(s)):  # Right pointer iterates over string
            # Shrink window from left if duplicate character found
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1

            char_set.add(s[r])                   # Add current character
            max_len = max(max_len, r - l + 1)    # Update max length

        return max_len
        