from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        
        for i in range(len(word)):
            new_word = word[:i] + word[i+1:]

            freq = Counter(new_word)

            freq_values = list(freq.values())

            if len(set(freq_values)) == 1:
                return True

        return False