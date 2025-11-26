class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return nums[-1]

        sett = set()
        for n in nums:
            if n not in sett:
                sett.add(n)

        final = sorted(list(sett), reverse=True)  # sort descending

        if len(final) < 3:
            return final[0]  # return max if less than 3 distinct numbers
        return final[2]