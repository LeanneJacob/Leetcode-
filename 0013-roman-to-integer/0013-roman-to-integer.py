class Solution:
    def romanToInt(self, s: str) -> int:
        summ=0
        mapp={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        i=0
        while i<len(s):
            if i+1< len(s) and mapp[s[i]]< mapp[s[i+1]]:
                r=mapp[s[i+1]]-mapp[s[i]]
                summ+=r
                i+=2
            else:
                summ+= mapp[s[i]]
                i+=1
        return summ
        