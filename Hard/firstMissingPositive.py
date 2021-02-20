'''
Given an unsorted integer array nums, find the smallest missing positive integer.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
'''
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = self.unique(nums)
        nums.sort()
        positive = 1
        for i,el in enumerate(nums):
            if el<=positive and el>0:
                positive +=1
        
        return positive
    
    def unique(self,nums):
        nums1 = []
        for el in nums:
            if el not in nums1:
                nums1.append(el)
        return nums1
