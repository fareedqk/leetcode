class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_count = 0
        for stone in stones:
            for jewel in jewels:
                if stone == jewel:
                    jewels_count += 1
        
        return jewels_count