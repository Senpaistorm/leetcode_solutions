# leetcode question 48: Rotate image
# You are given an n x n 2D matrix representing an image.

# Rotate the image by 90 degrees (clockwise).

# Note:

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.


class Solution:
    matrix1 =[
    [ 5, 1, 9,11],
    [ 2, 4, 8,10],
    [13, 3, 6, 7],
    [15,14,12,16]
    ]  
    matrix2 =[
    [7,4,1],
    [8,5,2],
    [9,6,3]
    ]
    matrix3 =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
    matrix4 = [
        [1,2],
        [3,4]
    ]

    def rotate(self, matrix: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify matrix in-place instead.
        """
        # keep four pointers starting at the corners
        n = len(matrix)
        # keep track of current state
        m = 0
        if n ==1: return
        # swap function that rotates four corresponding points 90 degrees
        def rotateFour(tl, tr, bl, br):
            (matrix[tl[0]][tl[1]], matrix[tr[0]][tr[1]], matrix[bl[0]][bl[1]], matrix[br[0]][br[1]]) = \
             (matrix[bl[0]][bl[1]], matrix[tl[0]][tl[1]], matrix[br[0]][br[1]], matrix[tr[0]][tr[1]])
        tl = [0,0] # from 0,0  
        tr = [0,n-1] # from 0, n-1 
        bl = [n-1,0] # from n-1, 0
        br = [n-1,n-1] # from n-1, n-1
        # we will stop when all matrices are rotated 
        # m = number of rings that are rotated
        while n > 2 * m + 1:
            while tl[1] != n-m-1:
                rotateFour(tl, tr, bl, br)
                tl[1] += 1
                tr[0] += 1
                bl[0] -= 1
                br[1] -= 1
            m += 1
            tl = [m, m]
            tr = [m, n-1-m]
            bl = [n-1-m, m]
            br = [n-1-m, n-1-m]


sol = Solution()
sol.rotate(sol.matrix1)
print(sol.matrix1)
sol.rotate(sol.matrix2)
print(sol.matrix2)
sol.rotate(sol.matrix3)
print(sol.matrix3)
sol.rotate(sol.matrix4)
print(sol.matrix4)