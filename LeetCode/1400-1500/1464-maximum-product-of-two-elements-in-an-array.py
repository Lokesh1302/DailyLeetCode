class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        total = len(nums) - 1
        return (nums[total] - 1) * (nums[total - 1] - 1)
