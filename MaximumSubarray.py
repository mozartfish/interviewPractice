# runtime complexity - O(n) since we do a single pass through the list
# space complexity - O(1) additional space since we do not use any other data structures
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        curr_sum = max_sum = nums[0]
        
        for i in range(1, n):
            curr_sum = max(nums[i], curr_sum + nums[i]) 
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
            