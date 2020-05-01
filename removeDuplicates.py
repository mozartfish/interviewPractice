class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        length = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[j - 1]:
                nums[length] = nums[j]
                length += 1
        return length
        