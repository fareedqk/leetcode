class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = (num * num for num in nums)
        result = sorted(result)
        return result

        