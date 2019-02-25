# LC question 814 
# We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.

# Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

# (Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        
        def containOne(root):
            l = False
            r = False
            if not root: return False
            if root.left:
                l = containOne(root.left)
            if root.right:
                r = containOne(root.right)
            return root.val == 1 or l or r
        
        def pruneRoot(root):
            
            if root.left:
                if containOne(root.left):
                    root.left = pruntRoot(left)
                else:
                    root.left = None
            if root.right: 
                if containOne(root.right):
                    root.right = pruneRoot(root.right)
                else:
                    root.right = None
            if not root.left and not root.right:
                if not root or root.val == 0:
                    return None
                else:
                    return root
            return root
        return pruneRoot(root)