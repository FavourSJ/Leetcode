class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        for i in range(len(strs[0])): #iterate through the first string index 1
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return result
            result += strs[0][i]
        
        return result