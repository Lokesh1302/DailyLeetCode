class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        target = 1
        for num in nums:
            if num <= 0:
                continue
            if num == target:
                target += 1
            else:
                return target
        return target
