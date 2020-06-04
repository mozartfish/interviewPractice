# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Runtime Complexity: O(n)
# Space Complexity: O(n) since we create a stack of size n 

# solution 1
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, inorder = [], float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        
        return True

# Runtime Complexity: O(n)
# Space Complexity: O(n) since we create a stack of size n 

# solution 2
# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         return self.helper(root)
    
#     def helper(self, node: TreeNode, low=float('-inf'), high=float('inf')):
#         if not node:
#             return True
        
#         val = node.val
#         if val <= low or val >= high:
#             return False
        
#         if not self.helper(node.right, val, high):
#             return False
        
#         if not self.helper(node.left, low, val):
#             return False
        
#         return True
        
        