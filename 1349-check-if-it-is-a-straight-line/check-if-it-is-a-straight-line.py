class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
# working out the initial gradient from first 2 points
        (x0, y0), (x1, y1) = coordinates[:2]

# iterate over all points (coordinates) in the List
        for x, y in coordinates:
            if (x1 - x0) * (y - y1) != (x - x1) * (y1 - y0):
# if the condition fails, the points don't have the same gradient
                return False
# if all points satisfy the condition -> straight line :)
        return True