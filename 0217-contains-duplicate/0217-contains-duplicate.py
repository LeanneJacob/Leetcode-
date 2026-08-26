class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count={}
        for char in nums:
            count[char]= count.get(char,0)+1

            if count[char]>1:
                return True
        return False