class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        indx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[indx] = nums[i]
                indx += 1
        
        for j in range(indx, len(nums)):
            nums[j] = 0 