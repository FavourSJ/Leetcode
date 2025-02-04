class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        CurrentAltitude = 0
        HighestPoint = CurrentAltitude

        for AltitudeGain in gain:
            CurrentAltitude = CurrentAltitude + AltitudeGain
            HighestPoint = max(HighestPoint,CurrentAltitude)

        return HighestPoint


        