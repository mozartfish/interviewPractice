class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_map = dict()
        for i, value in enumerate(nums):
            difference = target - value
            if difference in value_map:
                return [value_map[difference], i]
            value_map[value] = i