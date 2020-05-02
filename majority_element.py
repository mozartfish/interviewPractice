class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = nums[0]
        i = 0
        
        for j in range(len(nums)):
            if i == 0:
                m = nums[j]
                i = 1
            elif m == nums[j]:
                i = i + 1
            else:
                i = i - 1
        return m
                