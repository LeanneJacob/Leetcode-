class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Always binary search the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        while left <= right:
            cut1 = (left + right) // 2
            cut2 = (m + n + 1) // 2 - cut1

            # Elements immediately around the partitions
            left1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            right1 = float('inf') if cut1 == m else nums1[cut1]

            left2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            right2 = float('inf') if cut2 == n else nums2[cut2]

            # Correct partition
            if left1 <= right2 and left2 <= right1:

                # Odd total length
                if (m + n) % 2 == 1:
                    return max(left1, left2)

                # Even total length
                return (max(left1, left2) + min(right1, right2)) / 2

            # We need to move partition in nums1 right
            elif left1 > right2:
                right = cut1 - 1

            # We need to move partition in nums1 left
            else:
                left = cut1 + 1
        