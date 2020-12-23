'''
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_str = ''
        n = [len(s) - 1]

        for diff in range(1, len(s)):
            n.append(n[0] + diff)
            n.append(n[0] - diff)

        for i in n:
            if (min(i + 1, 2 * len(s) - 1 - i) <= len(longest_str)):
                break

            if i % 2 == 0:
                left, right = (i // 2) - 1, (i // 2) + 1
            else:
                left, right = i // 2, (i // 2) + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            if right - left - 1 > len(longest_str):
                longest_str = s[left + 1: right]

        return longest_str
