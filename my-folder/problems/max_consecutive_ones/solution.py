class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones_count = 0
        max_ones = 0
        for i in nums:
            if i != 1:
                ones_count = 0
            else:
                ones_count += 1
            # max_ones = max(max_ones, ones_count)
            if ones_count > max_ones:
                max_ones = ones_count
        return max_ones
        