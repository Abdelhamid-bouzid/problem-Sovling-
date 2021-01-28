'''
You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
'''
class Solution:
    def findSubstring(self, S, L):
        ans  = []
        Dict = Counter(L)      
        
        totWord = len(L)
        wordLen = len(L[0])
        slen =len(S) - totWord * wordLen;
        for  i in range(0,slen+1):
            ll    = Counter([S[i+k*wordLen:i+(k+1)*wordLen] for k in range(totWord)])
            if ll==Dict:
                ans.append(i)
        
        return ans
    
        
        
