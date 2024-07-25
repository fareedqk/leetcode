class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # map = {}
        # for i in nums:
        #     map[i] = i
        # # print(map)
        # for num in range(len(nums)):
        #     if num not in map:
        #         return num
        # return len(nums)
        
        size = len(nums)
        exp_total = size * (size+1) // 2
        total_sum = sum(nums)
        return exp_total - total_sum
