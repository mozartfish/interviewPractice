class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hmap = dict()
        for num in nums1:
            if num not in hmap:
                hmap[num] = 0
            hmap[num] += 1
        
        result = []
        for num in nums2:
            if num in hmap and hmap[num] > 0:
                hmap[num] -= 1
                result.append(num)
        
        return result
                