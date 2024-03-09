class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        left, right = 0, 0

        size1, size2 = len(nums1), len(nums2)

        while left < size1 and right < size2:
            if nums1[left] == nums2[right]:
                return nums1[left]
            
            if nums1[left] < nums2[right]:
                left += 1
            else:
                right += 1
        return -1

# Two pointer approach, where I start both the pointers and compare them
# If any of the value is less than the other one, Just move it to next index.
# If any of them goes out of bounds, return -1
