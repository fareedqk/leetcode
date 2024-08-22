class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr = []
        add = 0
        for i in nums:
            add = add + i
            arr.append(add)
        return arr
        