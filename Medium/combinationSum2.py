'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        comb, results = [], []
        self.backtrack(candidates,comb, target, 0, results)

        return results
    
    def backtrack(self,candidates,comb, remain, curr, results):

        if remain == 0:
            # make a deep copy of the resulted combination
            results.append(list(comb))
            return

        for next_curr in range(curr, len(candidates)):

            if next_curr > curr \
              and candidates[next_curr] == candidates[next_curr-1]:
                continue

            pick = candidates[next_curr]
            # optimization: skip the rest of elements starting from 'curr' index
            if remain - pick < 0:
                break

            comb.append(pick)
            self.backtrack(candidates,comb, remain - pick, next_curr + 1, results)
            comb.pop()
