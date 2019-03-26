# leetcode contest 123 question 992: Sub arrays with K Different Integers

# Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.

# (For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

# Return the number of good subarrays of A.

 

# Example 1:

# Input: A = [1,2,1,2,3], K = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
# Example 2:

# Input: A = [1,2,1,3,4], K = 3
# Output: 3
# Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
 

# Note:

# 1 <= A.length <= 20000
# 1 <= A[i] <= A.length
# 1 <= K <= A.length

# First intuition: brute force => for every element check substring containing itself, when the number of distinct
# elements is larger than K move on to the next element
# Since this was the last question I ran out of time to optimize this solution but I think it could work without
# breaking the time limit

# better solution: Sliding window
# Intuition:
# Write a helper using sliding window,
# to get the number of subarrays with at most K distinct elements.
# Then f(exactly K) = f(atMost K) - f(atMost K-1).

# Of course, you can merge 2 for loop into ones, if you like.

# Time Complexity:
# O(N)
import collections 

class Solution:
    def subarraysWithKDistinct(self, A: 'List[int]', K: 'int') -> 'int':
        
        
        def atMostK(A, K):
            res = i = 0 # result and i variable
            count = collections.Counter()
            for j in range(len(A)):
                if count[A[j]] == 0: # encounter a new int, decrement K
                    K -= 1
                count[A[j]] += 1 # increment the number of occurrences of A[j]
                while K < 0: # if we reached K distinct ints, move left pointer
                    count[A[i]] -= 1
                    if count[A[i]] == 0: K += 1
                    i += 1  
                res += j - i + 1 # the total number of subarrays will be right-left+1 
            #print(res)
            return res
        return atMostK(A, K) - atMostK(A, K-1)

sol = Solution()
print(sol.subarraysWithKDistinct([1,2,1,2,3],2))
print(sol.subarraysWithKDistinct([1,2,1,3,4],3))    