class Solution:
    def singleNumber(self, nums: List[int]) -> int:        
        result = {}
        for i in nums:
            result[i] = result.get(i, 0) + 1
        for key, value in result.items():
            if value == 1:
                return key