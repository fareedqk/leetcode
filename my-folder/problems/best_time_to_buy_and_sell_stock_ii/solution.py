class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                curr_profit = prices[i] - prices[i-1]
                total_profit += curr_profit
        return total_profit
        