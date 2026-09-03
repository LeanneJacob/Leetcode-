class Solution:
    def firstUniqChar(self, s: str) -> int:
        mapp={}
        for char in s:
            mapp[char]=mapp.get(char,0)+1
        
        for i in range(len(s)):
            if mapp[s[i]]==1:
                return i
        return -1
            
        