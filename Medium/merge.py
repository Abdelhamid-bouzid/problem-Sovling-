'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        st = [el[0] for el in intervals]
        inds = [i[0] for i in sorted(enumerate(st), key=lambda x:x[1])]
        new_int = [intervals[i] for i in inds]
        
        unique_int = [new_int[0]]
        for el in new_int[1:]:
            if el[0]<= unique_int[-1][-1]:
                if el[1]>unique_int[-1][-1]:
                    unique_int[-1][-1] = el[1]
            else:
                unique_int.append(el)
                
        return unique_int
            
        
