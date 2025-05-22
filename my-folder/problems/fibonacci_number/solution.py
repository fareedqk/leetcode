class Solution:
    def fib(self, n: int) -> int:
        memo = {}

        def helper(k):
            if k <= 1:
                return k
            if k not in memo:
                memo[k] = helper(k - 1) + helper(k - 2)
            return memo[k]
        
        return helper(n)