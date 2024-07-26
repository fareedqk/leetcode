class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # map = {}
        # for i in nums1:
        #     if i in nums2:
        #         map[i] = i
        # return map
        # return set(nums1) & set(nums2)
        res = []
        for i in nums1:
            if i in nums2 and i not in res:
                res.append(i)
        return res