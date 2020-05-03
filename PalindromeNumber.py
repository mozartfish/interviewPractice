class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = str(x)
        if original == original[::-1]:
            return True
        return False