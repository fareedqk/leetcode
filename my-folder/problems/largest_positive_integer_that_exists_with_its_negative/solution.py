class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        k = -1

        for i in nums:
            if - i in nums and k < i:
                k = i
        return k
