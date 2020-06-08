
# Runtime complexity: O(log n)
# Space Complexity: O(1) additional space
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        power = 0
        
        if n == 0:
            return False
        while n % 2 == 0:
            n /= 2
        
        return n == 1