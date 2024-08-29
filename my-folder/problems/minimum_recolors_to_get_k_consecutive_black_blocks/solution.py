class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites = blocks[:k].count("W")
        minimum = whites
        right = k - 1
        left = 0 
        length = len(blocks)

        if length == 1:
            return whites
        while right < length - 1:
            left += 1
            right += 1
            if blocks[left-1] == "W":
                whites -= 1
            if blocks[right] == "W":
                whites += 1
            minimum = min(minimum, whites)
        return minimum
