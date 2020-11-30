class Solution:
    def twoSum(self, nums: List[int], target: int):
        
        d = {}
        for index,val in enumerate(nums):
            
            if (target-val) in d:
                return [d[target-val],index]
            d[val] = index
