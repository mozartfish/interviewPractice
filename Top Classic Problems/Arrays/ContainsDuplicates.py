class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # sort the list 
        nums.sort()
        for i in range(len(nums)):
            if i + 1 == len(nums):
                return False
            if nums[i] == nums[i + 1]:
                return True        