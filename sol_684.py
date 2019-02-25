# leet code question 684: Redundant Connection
# In this problem, a tree is an undirected graph that is connected and has no cycles.

# The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

# The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.

# Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.

# intuition: an edge i,j is redundant if there exist edges x,i and y,j in the same
# graph, so we can find all the outward nodes of the graph, put them in a hash set
# then we loop backwards from the given array, if both elements are in the array, return 
# that subarray

class Solution:
    def findRedundantConnection(self, edges: 'List[List[int]]') -> 'List[int]':
        outerNodes = set()
        for edge in edges:
            outerNodes.add(edge[1])
        for i in range(len(edges)-1,-1,-1):
            if edges[i][0] in outerNodes and edges[i][1] in outerNodes:
                return edges[i]
        return None

# Example 1:
# Input: [[1,2], [1,3], [2,3]]
# Output: [2,3]
# Explanation: The given undirected graph will be like this:
#   1
#  / \
# 2 - 3
sol = Solution()
print(sol.findRedundantConnection([[1,2],[1,3],[2,3]]))        

print(sol.findRedundantConnection([[1,2],[1,3],[2,3],[2,4],[4,5],[5,6]]))      