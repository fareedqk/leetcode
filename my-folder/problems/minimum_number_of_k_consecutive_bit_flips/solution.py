class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        flip = 0
        q = deque()
        for i in range(len(nums)):
            if q and q[0] < i:
                q.popleft()
            if len(q) % 2 == nums[i]:
                if i+k-1 >= len(nums):
                    return -1
                q.append(i+k-1)
                flip += 1
        return flip