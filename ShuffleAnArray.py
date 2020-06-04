# Runtime Complexity: reset - O(1) since we are returning the underlying storage which is constant time
# shuffle - O(n) where n represents the number of elements in the list used in the function

# Space Complexity - shuffle - O(n) but there might be an additional cost due to the shallow copy with python


import math
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.storage = nums
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.storage
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        result = []
        nums_copy= copy.copy(self.storage)
        m = len(nums_copy)
        
        while m:
            i = math.floor(random.random() * m)
            m -= 1
            t = nums_copy[m]
            nums_copy[m] = nums_copy[i]
            nums_copy[i] = t
        
        return nums_copy
                
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()