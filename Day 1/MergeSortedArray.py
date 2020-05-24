class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # solution 1: Runtime Complexity: O(length of nums1) => faster solution
        # Space Complexity: O(n) since we do not allocate any other space
        # set up zero based counting for the size
        m -= 1
        n -= 1
        
        index = len(nums1) - 1 # get the last element
        
        while index >= 0:
            if m < 0:
                nums1[index] = nums2[n]
                n -= 1
            elif n < 0:
                nums1[index] = nums1[m]
                m -= 1
            else:
                if nums1[m] > nums2[n]:
                    nums1[index] = nums1[m]
                    m -= 1
                else:
                    nums1[index] = nums2[n]
                    n -= 1
                
            index -= 1

            # Solution 2: Runtime Complexity: O(n logn) where n is the total number of elements of the combined nums1 and nums2
            # Space complexity (m + n) since sorted returns a whole new list 
            nums1[:] = sorted(nums1[:m] + nums2)