# Runtime complexity: O(n * amount)
# Space complexity: O(amount) additional space
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        table = [0] * (amount + 1)
        table[0] = 1
        
        for coin in coins:
            for i in range(coin, amount + 1):
                table[i] += table[i - coin]
        return table[amount]
        