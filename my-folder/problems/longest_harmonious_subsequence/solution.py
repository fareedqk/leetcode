class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hash_map = {}
        for i in nums:
            hash_map[i] = hash_map.get(i, 0) + 1
        count = 0
        for num in hash_map:
            if num + 1 in hash_map:
                longest = hash_map[num] + hash_map[num+1]
                if longest > count:
                    count = longest
                # count = max(count, hash_map[num] + hash_map[num+1])
        return count

        # nums.sort()
        # left = 0
        # max_len = 0
        # for right in range(len(nums)):
        #     while nums[right] - nums[left] > 1:
        #         left += 1
        #     if nums[right] - nums[left] == 1:
        #         max_len = max(max_len, right - left + 1)
        # return max_len
            