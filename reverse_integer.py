class Solution:
    def reverse(self, x: int) -> int:
        # value for storing the result
        sum = 0
        
        # indicator for determining whether a value is positive or negative
        is_negative = False
        
        if x < 0:
            is_negative = True
            x = -1 * x
        
        number = str(x)
        num_list = [int(g) for g in number]
        for h in range(len(num_list)):
            if h == 0:
                sum += num_list[h]
                continue
            sum += num_list[h] * (10**h)
            
        if sum < 2**-31 or sum > 2**31:
            return 0
        
        if is_negative:
            sum *= -1
            
        return sum
            