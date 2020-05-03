class Solution:
    def romanToInt(self, s: str) -> int:
        # function for getting the digit representation of a roman numeral
        def num_int(character):
            switcher = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000,
            }
            return switcher.get(character, 0)
        
        sum = 0
        i = 0
        while i < len(s):
            num_char = s[i]
            first_num = num_int(num_char)
            second_val_index = i + 1
            if second_val_index < len(s):
                second_num= num_int(s[second_val_index])
                if first_num >= second_num:
                    sum += first_num
                    i += 1
                    
                else:
                    sum = sum + second_num - first_num
                    i += 2
            else:
                sum += first_num
                i += 1
        return sum 