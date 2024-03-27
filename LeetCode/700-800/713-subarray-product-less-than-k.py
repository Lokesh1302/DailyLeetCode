class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        start, end, size = 0, 0, len(nums)
        result, cur_product = 0, 1
        while end < size:
            cur_product *= nums[end]
            while cur_product >= k:
                cur_product = cur_product // nums[start]
                start += 1
            result += 1 + (end - start)     # This is very important step
            end += 1
        return result
