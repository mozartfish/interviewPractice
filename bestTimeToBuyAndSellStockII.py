class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # variable for keeping track of the max profit
        max_profit = 0
        for j in range(1, len(prices)):
            if prices[j] > prices[j - 1]:
                max_profit += prices[j] - prices[j - 1]
        return max_profit