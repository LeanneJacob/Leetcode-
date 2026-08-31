class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        result=[]
        mapp={}
        for num in nums2:
            while stack and num>stack[-1]:
                smaller=stack.pop()
                mapp[smaller]=num
            stack.append(num)
            

        for num in nums1:
            result.append(mapp.get(num,-1))
        return result
        