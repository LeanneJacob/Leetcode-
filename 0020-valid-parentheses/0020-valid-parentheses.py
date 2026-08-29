class Solution:
    def isValid(self, s: str) -> bool:
        #map contains closing brackets
        mapp={')':'(',']':'[','}':'{'}
        stack=[]
        for i in s:
            if i in mapp: # i is closing bracket?
                if not stack or stack[-1]!= mapp[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return len(stack)==0