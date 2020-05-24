# runtime complexity : O(n) where n represents the length of nums
# space complexity: O(1) since we are modifying the input list
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # variable for storing a counter which is also an index
        i = 0
        
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
            
        return i + 1