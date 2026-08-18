class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        # 1. Find the first decreasing element from the right
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 2. If such an element exists, find the next larger element
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1

            # Swap them
            nums[i], nums[j] = nums[j], nums[i]

        # 3. Reverse everything after i
        nums[i + 1:] = reversed(nums[i + 1:])