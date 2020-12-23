'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        string = ['' for i in range(numRows)]
        i = 0
        r = 0
        while i<len(s):
            if r<numRows:
                string[r] += s[i]
                r +=1
                i +=1

            else :
                j = numRows-2
                while i<len(s) and j>0:
                    string[j]+=s[i] 
                    j -=1
                    i +=1
                r = 0

        ss = ''.join(string)
        return ss
