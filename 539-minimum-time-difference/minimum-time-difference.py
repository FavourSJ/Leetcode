class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
# first sort the input times
        timePoints.sort()

# helper function to convert the input time to total minutes from 00:00
        def time_to_min(t):
            h, m = map(int, t.split(":"))
            return 60 * h + m

# result with the circular case (difference between first and last time across midnight)
        res = (
# total minutes in a day
            24 * 60 -
# convert last time to minutes
            time_to_min(timePoints[-1]) +
# convert first time to minutes
            time_to_min(timePoints[0])
        )

# iterate through sorted times to find the minimum adjacent difference
        for i in range(len(timePoints) - 1):
# convert current time to minutes
            cur = time_to_min(timePoints[i + 1])
# convert previous times to minutes
            prev = time_to_min(timePoints[i])
# find the difference
            diff = cur - prev
# update the result IF it is smaller
            res = min(res, diff)
# return the smallest difference
        return res