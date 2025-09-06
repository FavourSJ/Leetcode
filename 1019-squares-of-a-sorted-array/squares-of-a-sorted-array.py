class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared = []
        for num in nums:
            squared.append(num ** 2)
        return (sorted(squared))
        