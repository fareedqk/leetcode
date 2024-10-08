class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        total_ones = sum(nums)

        # edge cases 
        if total_ones == 0 or total_ones == n:
            return 0
        
        current_ones = sum(nums[:total_ones])
        max_ones = current_ones

        # sliding window using two pointers
        for i in range(n):
            current_ones -= nums[i]
            current_ones += nums[(i+total_ones) % n]
            max_ones = max(max_ones, current_ones)

        return total_ones - max_ones