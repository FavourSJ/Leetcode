# Time complexity O(n)
# Space complexity O(1)

class Solution:
    def romanToInt(self, s: str) -> int:
        # hashmap of 7 values representing the roman numerals
        roman = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        res = 0

        # for loop to iterate through each value
        for i in range(len(s)):
            # condition to check:
            # (1) number is within boundary
            # (2) the current number is greater than the next number
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                # if so minus it from answer
                res -= roman[s[i]]
                # if not add it to the total
            else:
                res += roman[s[i]]
        # return final result
        return res
        