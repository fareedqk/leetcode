class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for i in nums:
            # print(i)
            if i in seen:
                return True
            seen.add(i)
        return False

        