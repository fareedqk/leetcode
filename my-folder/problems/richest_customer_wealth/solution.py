class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        res = []
        for i in accounts:
            add = sum(i)

            res.append(add)
        return max(res)
        