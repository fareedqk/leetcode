class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []

        previous = intervals[0]

        for i in intervals:
            if i[0] <= previous[1]:
                previous[1] = max(i[1], previous[1])
            else:
                merged.append(previous)
                previous = i
            
        merged.append(previous)

        return merged
        



        


