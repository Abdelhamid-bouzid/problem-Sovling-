'''
53. Maximum Subarray
Easy

14910

695

Add to List

Share
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp      = [0]*len(nums)
        dp[0]   = nums[0]
        max_num = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            if dp[i]>max_num: 
                max_num = dp[i]
        return max_num
        
        
