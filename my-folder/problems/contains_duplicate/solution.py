class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = set()

        for num in nums:
            if num in res: # duplicate exists
                return True
            res.add(num) # 1, 2, 3
        return False