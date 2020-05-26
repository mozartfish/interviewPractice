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


    # alternative solution
    # runtime - The cost of converting an integer to a string in python => O(n) for all the digits in the number
    # space time complexity: O(n) additional space since we are allocating an entire array of size n for the digits
        # def reverse(self, x: int) -> int:
        # if x >= 0:
        #     ans = int(str(x)[::-1])
        # else:
        #     ans = -int(str(-x)[::-1])
            
        # if ans < -2**31 or ans > 2**31 - 1:
        #     return 0
        # else:
        #     return ans