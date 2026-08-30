class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        mapp={}
        res=[]
        for num in nums2:
            while stack and num>stack[-1]:
                smaller= stack.pop()
                mapp[smaller]=num
            stack.append(num)
        
        for num in nums1:
            res.append(mapp.get(num,-1))

        return res

        
        