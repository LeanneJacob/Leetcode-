class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,num in enumerate(nums):
            comp=target-num
            if comp in seen:
                return [seen[comp],i]

            seen[num]=i
        