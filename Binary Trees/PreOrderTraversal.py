# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Runtime Complexity: O(n) for all the nodes in the tree
# Space Complexity: O(1) additional space 
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        stack, result = [root], []
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            if node.right is not None:
                stack.append(node.right)
            
            if node.left is not None:
                stack.append(node.left)
        
        return result
        