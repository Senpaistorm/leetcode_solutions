# leetcode question 33: search rotated array
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Your algorithm's runtime complexity must be in the order of O(log n).

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

import math
class Solution:
    def search(self, nums: 'List[int]', target: 'int') -> 'int':
        # left is the smallest of the larger sub array
        # right is the largest of the smaller array
        # is target is in between then return -1
        left = 0
        right = len(nums)-1
        if nums == []: return -1
        
        if target == nums[left]: return left
        if target == nums[right]: return right
        def binSearch(nums, left, right, target):
            mid = math.ceil((left+right)/2)
            while mid < right:
                # in the smaller array
                if nums[mid] == target:
                    return mid
                else:
                    if nums[mid] > target:
                        right = mid
                    else:
                        left = mid
                mid = math.ceil((left+right)/2)

            return -1
        # case 0: no rotation
        if nums[left] < nums[right]: return binSearch(nums, left, right, target)
        # case 1: in between smaller array and bigger array
        if target < nums[left] and target > nums[right]:
            return -1
        # case 2: equal to either left or right
        
        mid = math.ceil((right+left)/2)
        # case 3: potentially in bigger array
        if target > nums[left]:
            while mid < right:
                # in the smaller array
                if nums[mid] == target:
                    return mid
                elif nums[mid] < nums[len(nums)-1]:
                    right = mid
                else:
                    if nums[mid] > target:
                        right = mid
                    else:
                        left = mid
                mid = math.ceil((right+left)/2)
        # case 4: potentially in smaller array
        else:
            while mid < right:
                if nums[mid] == target:
                    return mid
                elif nums[mid] > nums[0]:
                    left = mid
                else:
                    if nums[mid] > target:
                        right = mid
                    else:
                        left = mid
                mid = math.ceil((right+left)/2)
        return -1

sol = Solution()
print(sol.search([4,5,6,7,9,10,15,17,0,1,2,3], 14), -1)
print(sol.search([5,4],5), 0)
print(sol.search([4,5],4), 0)
print(sol.search([5],3), -1)
print(sol.search([10,15,17,3,4,5,6,7,9,], 3), 3)

print(sol.search([10,15,17,3,4,5,6,7,9,], 15), 1)