'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Notice that the solution set must not contain duplicate quadruplets.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [], target = 0
Output: []
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        return self.ksum(nums,target,4)
        
    def ksum(self,nums,target,k):
        res = []
        if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
            return res
        if sum(nums)==target and len(nums)==k:
            return [nums]
        if k == 2:
            return self.twoSum(nums, target)
        
        for i in range(len(nums)):
            if i==0 or nums[i]!=nums[i-1]:
                k_1 = self.ksum(nums[i+1:],target-nums[i],k-1)
                for el in k_1:
                    res.append([nums[i]]+el)
        
        return res
    
    def twoSum(self, nums, target):
        
        res = []
        l,r = 0,len(nums)-1
        
        while l<r:
            sum = nums[l] + nums[r]
            if sum<target or (l>0 and nums[l]==nums[l-1]):
                l +=1
            elif sum>target or (r<(len(nums)-1) and nums[r]==nums[r+1]):
                r -=1
            else:
                if [nums[l],nums[r]] not in res:
                    res.append([nums[l],nums[r]])
                l +=1
                r -=1
                
        return res
            
        
