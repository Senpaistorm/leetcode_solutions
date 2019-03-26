# 101. Symmetric Tree
# Easy

# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3

# But the following [1,2,2,null,3,null,3] is not:

#     1
#    / \
#   2   2
#    \   \
#    3    3

# Note:
# Bonus points if you could solve it both recursively and iteratively. 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        left = [root.left]
        right = [root.right]
        while(len(left) > 0 and len(right) > 0):
            lt = left.pop(0)
            rt = right.pop(0)
            if lt and rt:
                if lt.val != rt.val:
                    return False
                else:
                    left.append(lt.left)
                    left.append(lt.right)
                    right.append(rt.right)
                    right.append(rt.left)
            elif lt or rt:
                return False                

        return True
        