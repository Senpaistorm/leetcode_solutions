# 701. Insert into a Binary Search Tree
# Medium

# Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

# Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def insert(root):
            if not root: return TreeNode(val)
            if root.val > val:
                root.left = insert(root.left)
            else:
                root.right = insert(root.right)
            return root
        return insert(root)