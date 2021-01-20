'''
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.rec(nums,[],[])
        
    def rec(self,nums,res,el):
        if len(nums)==0:
            res.append(el)
            return 
        res.append(el)
        for i in range(len(nums)):
            self.rec(nums[i+1:],res,el+[nums[i]])

        return res
