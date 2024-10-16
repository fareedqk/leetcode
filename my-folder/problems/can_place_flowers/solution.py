class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while i < len(flowerbed) and n > 0:
            if flowerbed[i] == 1:
                i += 2  # Skip next spot since a flower is planted at i
            elif i == len(flowerbed) - 1 or flowerbed[i + 1] == 0:
                # Plant a flower if it's the last spot or the next spot is empty
                n -= 1
                i += 2  # Move two steps forward since we just planted
            else:
                i += 3  # Skip to the next possible empty spot
        return n <= 0  # If all flowers are planted, return True