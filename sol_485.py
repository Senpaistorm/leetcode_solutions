# max-consecutive ones

class Solution():

    def maxConsecutiveOnes(self, nums):
        n = len(nums)
        dp = [0] * n

        for i in range(n-1, -1, -1):
            if nums[i]:
                if i == n-1:
                    dp[i] = 1
                else:
                    dp[i] = 1 + dp[i+1]
        
        return max(dp)

sol = Solution()
print("Actual  Expected")
print(sol.maxConsecutiveOnes([1,1,0,1,1,1]), 3)
print(sol.maxConsecutiveOnes([1,0,1]), 1)
print(sol.maxConsecutiveOnes([0]), 0)
