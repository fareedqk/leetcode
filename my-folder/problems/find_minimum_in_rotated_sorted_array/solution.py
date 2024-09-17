class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        min_val = float("inf")
        for i in range(len(nums)):
            mid = (left+right) // 2
            min_val = min(min_val, nums[mid])
            if nums[mid] >= nums[right]:
                left += 1
            else:
                right -= 1
        return min_val
