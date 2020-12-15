'''
Given an integer n, return the number of trailing zeroes in n!.

Follow up: Could you write a solution that works in logarithmic time complexity?

 

Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0
'''




class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n==0:
            return 0
        
        r = self.rec(n)
        c = 0
        for el in str(r)[::-1]:
            if el=='0':
                c +=1
            else:
                break
        return c
    
    def rec(self, n):
        if n==1:
            return 1
        return n*self.rec(n-1)
