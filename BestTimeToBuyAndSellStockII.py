# Runtime Complexity: O(n) because of the for loop
# Space Complexity: O(n) for all the elements in the list 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        
        return max_profit
        
        