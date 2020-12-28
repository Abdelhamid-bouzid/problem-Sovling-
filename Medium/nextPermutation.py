'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
Example 4:

Input: nums = [1]
Output: [1]
'''
class Solution(object):
    def nextPermutation(self, nums):
        
        i=j = len(nums)-1
        while i>0 and nums[i]<=nums[i-1]:
            i -=1
        
        i -=1
        if i<0:
            nums.reverse()
            return
        
        while j>i and nums[j]<=nums[i]:
            j -=1
        
        nums[i],nums[j] = nums[j],nums[i]
        
        k,l = i+1, len(nums)-1
        
        while k<l:
            nums[k],nums[l] = nums[l], nums[k]
            k+=1
            l-=1
