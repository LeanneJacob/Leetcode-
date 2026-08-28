class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans=nums[-1]-nums[0]
        for i in range(len(nums)-1):
            high= max(nums[i]+k,nums[-1]-k)
            low=min(nums[0]+k,nums[i+1]-k)
            ans=min(ans,high-low)
        return ans

        """
        2, 2 , 7
        ans=5
        high=max(7,6)--7
        low=min(3,1)--1
        ans=5

        high=max(3,6)--6
        low=min(3,6)--3
        ans=3

        
        """


       