class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        for i in range(len(prices)-1):
            if max(prices[i+1:])-prices[i]>best_profit:
                best_profit = max(prices[i+1:])-prices[i]   
        return best_profit
