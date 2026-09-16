class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_buy = float('inf')
        

        for i in range(len(prices)):
            lowest_buy = min(prices[i], lowest_buy)
            max_profit = max(max_profit, prices[i] - lowest_buy)

        return max_profit