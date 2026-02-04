class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        i = 0
        n = len(s)

        # iterate through the strong to extact words
        while i < n:
            # skip leading spaces
            while i < n and s[i] == " ":
                i += 1
            # check if we have reached a word
            if i < n:
                # mark the start of a word
                word_start = i
                # find the end of the word
                while i < n and s[i] != " ":
                    i += 1
                # extract and store the word
                words.append(s[word_start:i]) 
        # Reverse the list of words and join them with single spaces
        return " ".join(words[::-1])