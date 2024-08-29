class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0
        for i in range(len(accounts)):
            addition = 0
            for j in range(len(accounts[i])):
                addition += accounts[i][j]
            if addition > wealth:
                wealth = addition
        
        return wealth
        