#LC Question 220: Contains Duplicate III

# GIven an array of int, find out whether there are two distinct indices i and j in the array such that the absolute diff
# between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        
        # n = len(nums)
        # # length of the array is less than 2 or k less than 1, always return False
        # if k < 1 or n < 2: return False
        # k = min(n,k)

        # # O(nk) solution
        # # double moving pointer
        # for j in range(n):
        #     for i in range(j+1, min(j+k+1,n) ,1):
        #         #print(j,i)
        #         # if abs is less than t, return True
        #         if abs(nums[j] - nums[i]) <= t:
        #             return True

        # # no possible answer found, return False
        # return False

        if k <= 0 or t < 0 or len(nums) < 2:
            return False

        min_val = min(nums)
        # normalize every element to >= 0
        if min_val < 0:
            nums = [n - min_val for n in nums]
            min_val = 0
        bucket_dict = {}
        # for every num in list
        for i, num in enumerate(nums):

            idx = int(num/(t+1))
            if len(bucket_dict) == k+1:
                bucket_dict.pop(int(nums[i-k-1]/(t+1)))
            if idx in bucket_dict:
                return True
            elif idx-1 in bucket_dict and num - bucket_dict[idx-1] <= t:
                return True
            elif idx+1 in bucket_dict and bucket_dict[idx+1] - num <= t:
                return True
            else:
                bucket_dict[idx] = num
        
        return False

sol = Solution()
print(sol.containsNearbyAlmostDuplicate([1,2,3,1], 3,0))
print(sol.containsNearbyAlmostDuplicate([1,0,1,1], 1,2))
print(sol.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2,3))
print(sol.containsNearbyAlmostDuplicate([1,7], 1,2))
print(sol.containsNearbyAlmostDuplicate([2,2],3,0))