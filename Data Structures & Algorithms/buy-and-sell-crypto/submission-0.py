class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        min_prices = float('inf')

        for i in range(n):
            if prices[i] < min_prices:
                min_prices = prices[i]

            if prices[i] - min_prices > profit:
                profit = prices[i] - min_prices

        return profit

            
        
        