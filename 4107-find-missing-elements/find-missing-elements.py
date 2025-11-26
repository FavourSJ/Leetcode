class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ordered = sorted(nums)
        ans = []

        minnum = ordered[0]
        maxnum = ordered[-1]

        arr = list(range(minnum, maxnum))

        for i in arr:
            if i not in ordered:
                ans.append(i)

        return ans