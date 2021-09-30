'''
392. Is Subsequence
Easy

3124

253

Add to List

Share
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        return self.rec(s,t)
    def rec(self,s,t):
        
        if len(t)<len(s):
            return False
        if s=='':
            return True
        
        if s[0]==t[0]:
            return self.rec(s[1:],t[1:])
        else:
            return self.rec(s,t[1:])
            
        
