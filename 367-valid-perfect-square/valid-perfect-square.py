class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = num

        while l <= r:
            middle = (l + r) // 2
            m_squared = middle * middle

            if m_squared == num:
                return True
            elif m_squared < num:
                l = middle + 1
            elif m_squared > num:
                r = middle - 1
        return False