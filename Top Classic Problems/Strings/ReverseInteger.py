class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        reversedInteger = 0
        if x < 0:
            sign = -1
            x = -1 * x
        
        while x != 0:
            digit = x % 10
            reversedInteger = reversedInteger * 10 + digit
            x = (x - digit) // 10
            
        if reversedInteger > (2**31 - 1) or reversedInteger < (-2**31 - 1):
            return 0
        
        return sign * reversedInteger
            