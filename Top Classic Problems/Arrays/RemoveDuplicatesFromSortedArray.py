class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # two pointer method to keep track of unique value and current index
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        # since we use 0 based counting, length is always 1 more than the counter 
        return i + 1
        