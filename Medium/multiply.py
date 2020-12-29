'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        if num1 == '0' or num2 == '0':
            return '0'
        
        ans = 0
        for i, n1 in enumerate(num2[::-1]):
            
            ###################################################################
            pre  = 0
            curr = 0
            for j, n2 in enumerate(num1[::-1]):
                multi = (ord(n1) - ord('0')) * (ord(n2) - ord('0'))
                first, second = multi // 10, multi % 10
                curr += (second + pre) * (10 ** j) 
                pre = first
            curr += pre * (10 ** len(num1))
            ###################################################################
            
            ans += curr * (10 ** i)
        return str(ans)
        
