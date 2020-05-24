# Runtime Complexity: O(log n) for the decimal to binary conversion + O(n) for the for loop
# space complexity: O(n) for the number of characters in the binary string
class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        bin_val = bin(n)
        for i in range(2, len(bin_val)):
            if bin_val[i] == "1":
                counter += 1
        
        return counter
        