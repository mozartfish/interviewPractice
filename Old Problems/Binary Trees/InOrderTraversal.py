# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Runtime Complexity: O(n) for going through all the nodes in the tree
# Space Complexity: O(1) additional space
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        stack, result = [], []
        
        curr_node = root
        while curr_node is not None or stack:
            while curr_node is not None:
                stack.append(curr_node)
                curr_node = curr_node.left
            curr_node = stack.pop()
            result.append(curr_node.val)
            curr_node = curr_node.right
        
        return result
        