# leetcode question 15: 3Sum

# find all elements in triplets [a,b,c] in nums such that a+b+c = 0
# brute force: O(n^3)
# idea: have three pointers and three nested loops, check against each combination of numbers
#       while keeping track of duplicate triplets
# Using twoSum: O(n^2)
# idea: use two sum(find all pairs of numbers that add up to n) for every element in
#       nums, with n = -nums[i] <-- the inverse of current num
#       add to our res array everytime a triplet adds up to 0

class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        nums = sorted(nums)
        res = []


        def twoSum(nums, n, l, r):
            res = []
            # l = 0 #left pointer
            # r = len(nums)-1 #right pointer
            while l < r:
                sumlr = nums[l] + nums[r] 
                if sumlr == n:
                    res.append([nums[l],nums[r]])
                    l += 1
                elif sumlr < n:
                    l += 1
                else:
                    r -= 1
            return res

        for i in range(len(nums)):
            left = i+1
            right = len(nums) - 1
            inv = -nums[i]
            twoSums = twoSum(nums, inv, left, right)

            if len(twoSums) > 0:
                for s in twoSums:
                    s.append(nums[i])
                    if s not in res:
                        res.append(s)

        for i in range(len(res)):
            res[i] = list(res[i])
        
        return res

sol = Solution()
print(sol.threeSum([1,1,1,2,3,-1,-2,-4,-6]))
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))