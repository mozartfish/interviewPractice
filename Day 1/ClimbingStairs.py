# Runtime Complexity: O(n) because of one for loop and iterating over the elements from 3 to the end
# Space Complexity: 0 (n) because the memo table is the size of n + 1 
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        memo_table = [0 for i in range(n + 1)]
        memo_table[1] = 1
        memo_table[2] = 2
        
        for j in range(3, n + 1):
            memo_table[j] = memo_table[j - 1] + memo_table[j - 2]
        
        return memo_table[n]
        