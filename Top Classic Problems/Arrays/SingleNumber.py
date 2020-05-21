class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while i in range(len(nums)):
            value = nums[i]
            sub_arr = nums[i + 1:]
            if value in sub_arr:
                i = sub_arr.index(value)
                nums = sub_arr[i + 1:]
            else:
                return nums[i]