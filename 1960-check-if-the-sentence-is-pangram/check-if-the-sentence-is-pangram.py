# Time Complexity: O(N)
# Space Complexity: 0(N)

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
        