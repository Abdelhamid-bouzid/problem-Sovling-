'''
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input: s = "adceb", p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input: s = "acdcb", p = "a*c?b"
Output: false
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_length = len(s)
        p_length = len(p)

        # Initialize dp
        dp = [[False] * (p_length+1) for _ in range(s_length + 1)]

        # Initialize dp[0][0], indicating that empty pattern matches empty string
        dp[0][0] = True

        # Initialize dp[0][j], non null pattern matches empty string
        for j in range(1, p_length+1):
            if p[j-1] != "*":
                break
            dp[0][j] = True
        
        for i in range(1, s_length+1):
            for j in range(1, p_length+1):
                # Into the transfer equation
                if p[j-1] == s[i-1] or p[j-1] == "?":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        
        return dp[s_length][p_length]
