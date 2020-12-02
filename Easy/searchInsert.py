class Solution:
    def searchInsert(self, nums: List[int], target: int):
        
        i = 0
        while i<len(nums):
            if nums[i]==target or target<nums[i]:
                break
            i+=1
        return i
