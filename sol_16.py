# leetcode question 16: 3SumClosest
# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

# for every element i, we find the closest twosum from j to the end with respect 
# to target - i. When we get closer to the target, update the answer

class Solution:
    def threeSumClosest(self, nums: 'List[int]', target: 'int') -> 'int':
        if len(nums) < 3: return 0
        nums = sorted(nums)
        
        def twoSumClosest(nums, n, l, r):
            res = nums[l] + nums[r]
            # l = 0 #left pointer
            # r = len(nums)-1 #right pointer
            while l < r:
                sumlr = nums[l] + nums[r] 
                if sumlr == n:
                    res = sumlr
                    return res
                elif sumlr < n:
                    if abs(sumlr - n) < abs(res - n):
                        res = sumlr
                    l += 1
                else:
                    if abs(sumlr - n) < abs(res - n):
                        res = sumlr
                    r -= 1
            return res
        # set default ans
        ans = nums[0] + nums[1] + nums[len(nums)-1]
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1
            # compute closest twosum with respect to target - nums[i]
            threesum = nums[i] + twoSumClosest(nums, target-nums[i], left, right)
            # if it's closer to target than our ans, update ans
            if abs(threesum - target) < abs(ans - target):
                ans = threesum

        return ans

sol = Solution()
# Example:
# Given array nums = [-1, 2, 1, -4], and target = 1.
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
print(sol.threeSumClosest([-1,2,1,-4], 1))