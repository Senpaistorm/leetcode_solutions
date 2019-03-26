# 300. Longest Increasing Subsequence
# Medium

# Given an unsorted array of integers, find the length of longest increasing subsequence.

# Example:

# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

# Note:

#     There may be more than one LIS combination, it is only necessary for you to return the length.
#     Your algorithm should run in O(n2) complexity.

# Follow up: Could you improve it to O(n log n) time complexity?

class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        if n < 1: return n
        maxlen = 1
        dp = [1] * n

        # for every number
        for i,num in enumerate(nums):
            if i > 0:
                # loop backwards to connect with the longest subsequence
                for j in range(i-1, -1, -1):
                    if nums[i] > nums[j]:
                        if dp[j] + 1 > dp[i]:
                            dp[i] = dp[j] + 1
                            if dp[i] > maxlen:
                                maxlen = dp[i]
        return maxlen

sol = Solution()
print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]))
print(sol.lengthOfLIS([10,9,2,5,3,7,101,18,102]))
print(sol.lengthOfLIS([10,9]))
print(sol.lengthOfLIS([10,9,2,1,18]))
print(sol.lengthOfLIS([10]))