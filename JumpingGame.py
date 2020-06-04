# runtime complexity: O(n)
# space complexity: O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # find the last index
        last_index = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= last_index:
                last_index = i
        
        return last_index == 0

            