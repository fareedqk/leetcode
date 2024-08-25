class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, zeros, answer = 0, 0, 0

        for right in range(n):
            if nums[right] == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            answer = max(answer, right - left + 1 - zeros)
        
        return answer - 1 if answer == n else answer



        