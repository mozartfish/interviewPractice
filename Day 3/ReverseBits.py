# Runtime Complexity: O(log(n)) due to shifting the bits left and right
# Space Complexity: O(1) additional space since we don't use any other data structures 

class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        for _ in range(32):
            tmp = n&1
            n = n>>1
            ret = ret<<1
            ret += tmp
            
        return ret