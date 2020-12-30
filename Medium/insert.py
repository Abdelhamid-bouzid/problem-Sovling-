'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
Example 3:

Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]
Example 4:

Input: intervals = [[1,5]], newInterval = [2,3]
Output: [[1,5]]
Example 5:

Input: intervals = [[1,5]], newInterval = [2,7]
Output: [[1,7]]
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        st = len(intervals)
        for i,el in enumerate(intervals):
            if el[0]>newInterval[0]:
                st = i
                break
        
        intervals = intervals[:st] + [newInterval]+ intervals[st:]
        
        ans = [intervals[0]]
        for el in intervals:
            if el[0]>ans[-1][-1]:
                ans.append(el)
            else:
                ans[-1][0]  = min(el[0],ans[-1][0])
                ans[-1][-1] = max(el[1],ans[-1][-1])
                
        return ans
        
