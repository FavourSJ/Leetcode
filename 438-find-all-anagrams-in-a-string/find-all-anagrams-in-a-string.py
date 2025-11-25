# sliding window solution

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_p = len(p)
        len_s = len(s)
        if len_p > len_s:
            return []

        # frequency of characters in p
        p_count = Counter(p)
        # initial window in s
        window_count = Counter(s[:len_p])

        res = []
        # check the first window
        if window_count == p_count:
            res.append(0)

        # slide the window across s
        for i in range(len_p, len_s):
            # start the character leaving the window
            start_char = s[i - len_p]
            # character entering the window
            end_char = s[i]

            # update the window character
            window_count[end_char] = window_count.get(end_char, 0) + 1
            window_count[start_char] -= 1
            if window_count[start_char] == 0:
                # remove zero count chars for clean comparison
                window_count.pop(start_char)

            # compare the current window with p
            if window_count == p_count:
                res.append(i - len_p + 1)

        return res