# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# runtime complexity - O(n) since we traverse the entire tree
# space complexity - O(1) additional space
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)
    
    def isMirror(self, left: TreeNode, right: TreeNode):
        if not left and not right:
            return True
        
        if not left and right:
            return False
        
        if left and not right:
            return True
        
        return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
        