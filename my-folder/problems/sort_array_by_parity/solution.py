class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for i in nums:
            if i%2 == 0:
                even.append(i)
            elif i%2 != 0:
                odd.append(i)
        return even + odd
        # l, r = 0, len(nums)-1
        # while l > r:
        #     if nums[l]%2 == 0 and nums[r]%2 != 0:
        #         nums[l], nums[r] = nums[r], nums[l]
        #         l += 1
        #         r -= 1
        # return nums