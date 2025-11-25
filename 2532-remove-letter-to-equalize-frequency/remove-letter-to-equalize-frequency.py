from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        # try removing each character once
        for i in range(len(word)):
            # build the strong after removing the i-th character
            new_word = word[:i] + word[i + 1:]
            # count the frequencies of remaining characters
            freq = Counter(new_word)
            # get all frequency values
            freq_values = list(freq.values())
            # check if all frequencies are the same
            if len(set(freq_values)) == 1:
                return True

        return False