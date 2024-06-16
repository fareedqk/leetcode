class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        map_list = defaultdict()
        good_pair = 0
        for num in nums:
            if num not in map_list:
                map_list[num] = 1
            else:
                good_pair += map_list[num]
                map_list[num] += 1
        
        return good_pair