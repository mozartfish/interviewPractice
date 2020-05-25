# Runtime Complexity: O(1) due to python optimizations but 
# I think it's O(log n) because bin function supposedly has a runtime of O(log n)
# Space Complexity: O(1) since no new data structure is created to store data

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')