class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        baskets = {}
        l = 0
        max_length = 0
        for r in range(len(fruits)):
            if fruits[r] not in baskets:
                baskets[fruits[r]] = 1
            else:
                baskets[fruits[r]] += 1
            if len(baskets) <= 2:
                max_length = max(max_length, r - l + 1)
            else:
                baskets[fruits[l]] -= 1
                if baskets[fruits[l]] == 0:
                    baskets.pop(fruits[l])
                l += 1
        return max_length