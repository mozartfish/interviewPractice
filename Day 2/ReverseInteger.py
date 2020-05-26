# Runtime complexity: O(n) where n represents the number of digits in the number
# space complexity: O(n) because of the size of the original input 
class Solution:
    def reverse(self, x: int) -> int:
        # variable for representing sign
        sign = 1
        reversed_int = 0
        
        # check if input value is less than 0
        if x < 0:
            sign = -1
            x *= -1
            
        while x != 0:
            digit = x % 10
            reversed_int = reversed_int * 10 + digit
            x = (x - digit) // 10
        
        if reversed_int < (-2**31 - 1) or reversed_int > (2**31 - 1): return 0
        
        return sign * reversed_int
            