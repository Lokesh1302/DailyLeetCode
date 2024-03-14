class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        table = {0 : 1}    # Prefix Sum and Frequency
        count, result = 0, 0
        for i in range(0, len(nums)):
            count += nums[i]
            target = count - goal  # this check has to be done before inserting because if k == 0 it will fail.
            if target in table:
                result += table[target]
            if count not in table:
                table[count] = 0
            table[count] += 1    
        return result




# https://leetcode.com/problems/subarray-sum-equals-k/
# Same Problem but binary array.
