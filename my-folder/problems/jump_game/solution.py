class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0

        for i in range(len(nums)):
            # current idx
            if i > max_jump:
                return False
            max_jump = max(max_jump, nums[i] + i)
        return max_jump >= len(nums)-1