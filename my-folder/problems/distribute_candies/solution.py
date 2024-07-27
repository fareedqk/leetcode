class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        map = {}
        for i in candyType:
            map[i] = i
        print(map)
        max_candies = len(candyType) // 2
        if len(map) > max_candies:
            return max_candies
        return len(map)
        