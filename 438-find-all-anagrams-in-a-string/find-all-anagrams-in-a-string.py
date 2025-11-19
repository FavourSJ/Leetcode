# sliding window solution

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_p = len(p)
        len_s = len(s)
        if len_p > len_s:
            return []

        p_count = Counter(p)           # Frequency of characters in p
        window_count = Counter(s[:len_p])  # Initial window in s

        res = []
        if window_count == p_count:    # Check first window
            res.append(0)

        # Slide the window across s
        for i in range(len_p, len_s):
            start_char = s[i - len_p]  # Character leaving the window
            end_char = s[i]            # Character entering the window

            # Update the window counter
            window_count[end_char] = window_count.get(end_char, 0) + 1
            window_count[start_char] -= 1
            if window_count[start_char] == 0:
                window_count.pop(start_char)  # Remove zero-count chars for clean comparison

            # Compare current window with p
            if window_count == p_count:
                res.append(i - len_p + 1)

        return res