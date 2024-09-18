class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        curr_sum = 0
        for i in nums:
            if curr_sum < 0:
                curr_sum = 0

            curr_sum += i
            result = max(result, curr_sum)
        return result