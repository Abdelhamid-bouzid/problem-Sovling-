class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        i=0
        while i<len(nums) and nums.count(nums[i])==2:
            i +=1
                
        return nums[i]
