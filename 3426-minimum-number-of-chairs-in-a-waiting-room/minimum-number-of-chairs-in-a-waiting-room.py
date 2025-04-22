class Solution:
    def minimumChairs(self, s: str) -> int:

        chairs = 0
        space = 0

        for i in s:
            if i == 'E':
                chairs += 1
            else:
                chairs -= 1
            space = max(space, chairs)
        return space
        