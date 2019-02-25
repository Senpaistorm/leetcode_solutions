# 94. Binary Tree Inorder Traversal
# Medium

# Given a binary tree, return the inorder traversal of its nodes' values.

# Example:

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [1,3,2]

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode):
        
        def inorder(root):
            if not root: return []
            ret = [root.val]
            if root.left:
                ret = inorder(root.left) + ret
            if root.right:
                ret = ret + inorder(root.right) 
            return ret
        return inorder(root)