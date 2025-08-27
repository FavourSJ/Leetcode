class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        char_to_word, word_to_char = {}, {}

        for i in range(len(pattern)):
            c = pattern[i]
            w = words[i]

            if (c in char_to_word) and (char_to_word[c] != w):
                return False
            else:
                char_to_word[c] = w

            if (w in word_to_char) and (word_to_char[w] != c):
                return False
            else:
                word_to_char[w] = c

        return True