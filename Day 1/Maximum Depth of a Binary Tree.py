# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Runtime Complexity: O(log n) where n represents the number of nodes in the tree
# Space Complexity: O(1) since we didn't use any additional space than what was given in the problem
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        # 
        if root is None:
            return 0
        
        right_depth = self.maxDepth(root.right)
        left_depth = self.maxDepth(root.left)
        
        return max(right_depth, left_depth) + 1
        