class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res = 0
        prev = values[0]
        for i in range(1, len(values)):
            res = max(res, prev + values[i] - i)
            prev = max(prev, values[i] + i)
        
        return res