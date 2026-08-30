from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        s1_count=Counter(s1)
        window_count= Counter(s2[:n])

        if n>len(s2):
            return False
        if s1_count== window_count:
            return True
        
        for i in range(n,len(s2)):
            window_count[s2[i]]+=1

            window_count[s2[i-n]]-=1

            if window_count[s2[i-n]]==0:
                del window_count[s2[i-n]]

            if s1_count== window_count:
                return True
        return False


        