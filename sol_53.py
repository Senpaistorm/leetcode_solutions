# LC question 53
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.


class Solution:
    def maxSubArray(self, nums):
        if len(nums) == 0: return 0

        maxSum = nums[0]
        for i,num in enumerate(nums):
            if i > 0:
                nums[i] = max(nums[i-1] + nums[i], nums[i])
                if nums[i] > maxSum:
                    maxSum = nums[i]
        return maxSum

            
sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))