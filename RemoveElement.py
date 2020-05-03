class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = 0
        
        for j in range(len(nums)):
            if nums[j] != val:
                nums[length] = nums[j]
                length += 1
        return length
        