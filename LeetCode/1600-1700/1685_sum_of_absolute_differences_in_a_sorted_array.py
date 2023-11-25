class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        right_sum = 0
        left_sum = 0
        for i in range(len(nums)):
            right_sum += nums[i]
        result = []
        length = len(nums)
        
        for cur_index in range(length):
            right_multiplier = length - cur_index
            right = right_sum - nums[cur_index] * right_multiplier

            left_multiplier = cur_index
            left = left_multiplier * nums[cur_index] - left_sum

            right_sum =  right_sum - nums[cur_index]
            left_sum = left_sum + nums[cur_index]

            result.append(right + left)
        
        return result
