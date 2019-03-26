# LC question 960
# We are given an array A of N lowercase letter strings, all of the same length.

# Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.

# For example, if we have an array A = ["babca","bbazb"] and deletion indices {0, 1, 4}, then the final array after deletions is ["bc","az"].

# Suppose we chose a set of deletion indices D such that after deletions, the final array has every element (row) in lexicographic order.

# For clarity, A[0] is in lexicographic order (ie. A[0][0] <= A[0][1] <= ... <= A[0][A[0].length - 1]), A[1] is in lexicographic order (ie. A[1][0] <= A[1][1] <= ... <= A[1][A[1].length - 1]), and so on.

# Return the minimum possible value of D.length.

class Solution(object):
    def minDeletionSize(self, A):
        # W is length of string
        W = len(A[0])
        # our dp array
        dp = [1] * W
        # from second last column to first colomn
        for i in range(W-2, -1, -1):
            # from i+1 to the end
            for j in range(i+1, W):
                # if everything between i to j is in lex order
                if all(row[i] <= row[j] for row in A):
                    # update dp[i] to be the number of elements we can keep from [i:]
                    dp[i] = max(dp[i], 1 + dp[j])

        return W - max(dp)

sol = Solution()
print(sol.minDeletionSize(["babca","bbazb"]))
# i = 3 j = 4 