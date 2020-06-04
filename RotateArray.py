# Runtime Complexity: O(n) since the reverse function goes through all the elements
# Space Complexity: O(1) additional space since we don't use any other data structures
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        
        # reverse all the numbers
        self.reverse(nums, 0, n - 1)
        # reverse the first k numbers
        self.reverse(nums, 0, k - 1)
        # reverse the numbers from k to the end
        self.reverse(nums, k, n - 1)
        
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
        