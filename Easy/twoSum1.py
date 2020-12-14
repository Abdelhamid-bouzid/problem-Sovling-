class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        d = {0: target - numbers[0]}
        i = 1
        while i< len(numbers):
            for index, val in d.items():  
                if val == numbers[i]:
                    return [index+1,i+1]
            else:
                d[i]=target - numbers[i]
            i +=1
