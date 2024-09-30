class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        result = -1

        while left <= right:
            mid = (left+right) // 2
            s = 0
            for i in range(len(nums)):
                s += math.ceil(nums[i]/mid)
            if s <= threshold:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result
