class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0 # left pointer
        for r in range(len(nums)): # traversing right pointer
            if nums[r]:
                nums[left], nums[r] = nums[r], nums[left] # swapping
                left += 1
            
        return nums
        