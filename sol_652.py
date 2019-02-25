# 652. Find Duplicate Subtrees
# Medium

# Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

# Two trees are duplicate if they have the same structure with same node values.

# Example 1:

#         1
#        / \
#       2   3
#      /   / \
#     4   2   4
#        /
#       4

# The following are two duplicate subtrees:

#       2
#      /
#     4

# and

#     4

# Therefore, you need to return above trees' root in the form of a list.

import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode):
        # to keep track of all duplicate subtrees
        res = []
        # counter to count each serialization
        count = collections.Counter()

        # we could serialize this tree at every node using dfs
        def serialize(root):
            # for none nodes, serialize it with #
            if not root: return '#'
            # serialize left and right
            ser = str(root.val) + serialize(root.left) + serialize(root.right)
            # increment counter for this specific tree
            count[ser] += 1
            # if counter reaches 2, add it to result list
            if count[ser] == 2:
                res.append(root)
            return ser
        
        serialize(root)
        return res



