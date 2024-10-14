class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0 # pointer 1
        for right in range(len(nums)):
            if nums[right] != 0:
                # swapping
                nums[left], nums[right] = nums[right], nums[left]
                # nums[left] = nums[right]
                # nums[right] = nums[left]
                left += 1 # left = left + 1

        