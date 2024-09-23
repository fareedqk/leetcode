class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height)-1
        while l < r: # O(N)
            area = min(height[l], height[r]) * (r - l) # O(1)
            res = max(res, area)
            if height[l] < height[r]: # O(1)
                l += 1
            # elif height[l] > height[r]:
            #     r -= 1
            else:
                r -= 1
        return res

        # Time: O(N)
        # Space: O(1)
        
        