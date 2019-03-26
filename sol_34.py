# leetcode question 34
# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# idea: implement helper functions that finds the left most index and right most index of target
import math
class Solution:
    def searchRange(self, nums: 'List[int]', target: 'int') -> 'List[int]':

        # find the left most index of target
        # importance is setting the right side to m when nums[m] == target
        def binaryLeft(nums, target):
            res = -1
            if nums[len(nums)-1] == target: res = len(nums)-1
            if nums[0] == target: return 0
            l = 0
            r = len(nums)-1
            m = math.ceil((l+r)/2)
            while r - l > 1:
                if nums[m] == target:
                    res = m
                    r = m
                elif nums[m] > target:
                    r = m
                else:
                    l = m
                m = math.ceil((l+r)/2) 
            return res

        # opposite idea of binaryLeft
        def binaryRight(nums, target):
            res = -1
            if nums[0] == target: res = 0
            if nums[len(nums)-1] == target: return len(nums)-1
            l = 0
            r = len(nums)-1
            m = math.ceil((l+r)/2)
            while r - l > 1:
                if nums[m] == target:
                    res = m
                    l = m
                elif nums[m] > target:
                    r = m
                else:
                    l = m
                m = math.ceil((l+r)/2) 
            return res
        if len(nums) == 0: return [-1,-1]
        if nums[0] == nums[len(nums)-1] == target: return [0,len(nums)-1]
        return [binaryLeft(nums, target), binaryRight(nums, target)]

sol = Solution()
print("Result,  Expected")
print(sol.searchRange([5,7,7,8,8,10], 8), [3,4])
print(sol.searchRange([5,7,7,8,8,10], 6), [-1,-1])
print(sol.searchRange([5,7,7,8,8,10], 10), [5,5])
print(sol.searchRange([5,7,7,8,8,10], 5), [0,0])
print(sol.searchRange([5,6,7,7,8,8,9,10], 9), [6,6])
print(sol.searchRange([5,6,7,7,8,8,9,10], 6), [1,1])
print(sol.searchRange([5,6,7,7,7,7,7,7,7,8,8,9,10], 7), [2,8])
print(sol.searchRange([1], 1), [0,0])
print(sol.searchRange([], 1), [-1,-1])
print(sol.searchRange([1,2,2], 2), [1,2])