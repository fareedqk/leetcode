class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]

        for i in nums:
            if (abs(closest) > abs(i)) or (abs(i) == abs(closest) and i > closest):
                closest = i
        return closest
        