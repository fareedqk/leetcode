class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        sorted_nums = sorted(nums, key=lambda x: (freq[x], -x))
        
        return sorted_nums
