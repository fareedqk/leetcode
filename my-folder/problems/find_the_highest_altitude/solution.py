class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        altitude = 0
        for val in gain:
            altitude += val
            if altitude > highest:
                highest = altitude
        
        return highest