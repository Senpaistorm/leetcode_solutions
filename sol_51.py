# LC question #51: N-queens

# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Each solution contains a distinct board configuration of the n-queens' pl
#acement, where 'Q' and '.' both indicate a queen and an empty space respectively.
import collections

class Solution:
    def solveNQueens(self, n: int):
        # user four counters to store board state
        row = collections.Counter()
        col = collections.Counter()
        # top to bottom diagonal
        diag1 = collections.Counter()
        # bottom to top diagonal
        diag2 = collections.Counter()
        # our result array
        res = []


        # for every slot in the first row, if the rest of the slots can construct
        # a valid solution, store it in the res array
        # row = k
        # col = i
        # diag1 = k-i
        # diag2 = k+i
        def validNQueen(k, queens, row, col, diag1, diag2):
            for i in range(n):
                if(row[k] or col[i] or diag1[k-i] or diag2[k+i]):
                    continue
                # we reached the last row, an answer has been found
                if(k == n-1): res.append(queens+[i])
                row[k] = 1
                col[i] = 1
                diag1[k-i] = 1
                diag2[k+i] = 1
                validNQueen(k+1, queens+[i], row, col, diag1, diag2)
                row[k] = 0
                col[i] = 0
                diag1[k-i] = 0
                diag2[k+i] = 0
        ans = validNQueen(0, [], row, col, diag1, diag2)
        if ans:
            res.add(constructBoard(ans))
        return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in res]
sol = Solution()
print(sol.solveNQueens(4))
print(sol.solveNQueens(8))