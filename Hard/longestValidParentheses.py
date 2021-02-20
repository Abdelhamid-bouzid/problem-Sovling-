'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        stack      = [-1]
        max_length = 0
        for i,el in enumerate(s):
            if el=="(":
                stack.append(i)
            else:
                stack.pop()
                if len(stack)==0:
                    stack.append(i)
                else:
                    max_length = max(max_length,i-stack[-1])
                    
        return max_length
