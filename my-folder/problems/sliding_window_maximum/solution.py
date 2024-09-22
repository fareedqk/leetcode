class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        result = []

        for i, n in enumerate(nums):
            while q and nums[q[-1]] < n: # pop smaller values
                q.pop()
            q.append(i)

            if q[0] == i - k: # Popped from left because it's outside the window's leftmost (i-k)
                q.popleft()

            if i >= k - 1:
                result.append(nums[q[0]])
        return result