class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        A = len(word1)
        B = len(word2)
        a, b = 0, 0
        s = []

        word = 1
        while a < A and b < B:
            if word == 1:
                s.append(word1[a])
                a += 1
                word = 2
            else:
                s.append(word2[b])
                b += 1
                word = 1

        while a < A:
            s.append(word1[a])
            a += 1
        
        while b < B:
            s.append(word2[b])
            b += 1
        
        return "".join(s)





















        m = len(word1)
        n = len(word2)
        i = 0
        j = 0
        result = []
        while i < m or j < n:
            if i < m:
                result += word1[i]
                i = i + 1
            if j < n:
                result += word2[j]
                j = j + 1

        return ''.join(result)

        