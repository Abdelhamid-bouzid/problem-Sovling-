class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        vally = prices[0]
        peak  = prices[0]
        i=0
        while i<len(prices)-1:
            while i<len(prices)-1 and prices[i]>=prices[i+1]:
                i+=1
                
            vally = prices[i]
            while i<len(prices)-1 and prices[i]<=prices[i+1]:
                i+=1
                
            peak      = prices[i]
            maxprofit += peak-vally
            
        return maxprofit
