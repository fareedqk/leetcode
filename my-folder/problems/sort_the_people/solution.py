class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        map = {}
        for i in range(len(names)):
            map[heights[i]] = names[i]
        
        heights.sort(reverse=True)
        for i in range(len(names)):
            names[i] = map[heights[i]]
        return names
        