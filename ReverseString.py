# runtime complexity: O(n) where n is the number of elements in the list
# space complexity: O(n) since we do not allocate any extra memory and use the input 

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # solution 1
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
        
        # solution 2 - Runtime Complexity might be O(1) because of the way python works under the hood
        s[:] = s[::-1]