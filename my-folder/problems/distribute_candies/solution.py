class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        unique_candies = set(candyType)
        
        max_candies = len(candyType) // 2

        return min(len(unique_candies), max_candies)
        