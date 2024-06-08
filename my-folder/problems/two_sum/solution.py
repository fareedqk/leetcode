class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        res = {}

        for i, num in enumerate(nums):
            comp = target - num
            print(comp)
            if comp in res:
                return [res[comp], i]
            res[num] = i



            