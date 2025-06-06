# Time Complexity O(N)
# Space Complexity O(1)

class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0

        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res