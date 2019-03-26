# 399. Evaluate Division
# Medium

# Equations are given in the format A / B = k, where A and B are variables represented as strings, 
# and k is a real number (floating point number). Given some queries, return the answers. If the answer
# does not exist, return -1.0.

# Example:
# Given a / b = 2.0, b / c = 3.0.
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
# return [6.0, 0.5, -1.0, 1.0, -1.0 ].

# The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> 
# queries , where equations.size() == values.size(), and the values are positive. This represents the equations.
# Return vector<double>.

# According to the example above:

# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 

# The input is always valid. You may assume that evaluating the queries will result in no division
# by zero and there is no contradiction. 
import collections

class Solution:
    def calcEquation(self, equations, values, queries):
        gragh = collections.defaultdict(dict)
        # make a graph with equations, values using defaultdict
        for (start, den), value in zip(equations, values):
            gragh[start][den] = value
            gragh[den][start] = 1 / value

        result = []

        # run dfs on every pair of queries
        for pair in queries:
            result.append(self.dfs(pair[0], pair[1], gragh, set()))

        return result

    #  x / y
    def dfs(self, x, y, gragh, visited):
        # if one of x/y is not in the graph, return -1
        if x not in gragh or y not in gragh:
            return -1.0
        # add x to visited vertices
        visited.add(x)
        # for all adjacency list of x
        for des, value in gragh[x].items():
            # if y is found, return value
            if y == des:
                return value
            # otherwise dfs on des, if des is not yet visited
            elif des not in visited:
                d = self.dfs(des, y, gragh, visited)
                # return x/des * des/.. ../y as our answer
                if d > 0:
                    return d * gragh[x][des]
        return -1.0
sol = Solution()
print(sol.calcEquation([ ["a","b"],["b","c"] ],[2.0,3.0],[ ["a","c"],["b","c"],["a","e"],["a","a"],["x","x"]]))


