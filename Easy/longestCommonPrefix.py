class Solution:
    def longestCommonPrefix(self, strs: List[str]):
        if len(strs)>201 or len(strs)==0:
            return ""
        
        prefix = strs[0]
        for string in strs[1:]:
            while string[:len(prefix)]!=prefix and prefix:
                prefix = prefix[:-1]
            if prefix=="":
                break
        return prefix
