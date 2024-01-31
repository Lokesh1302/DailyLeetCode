class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        table = {0 : -1}
        count, result = 0, 0
        for i in range(0, len(nums)):
            if nums[i] == 1:
                count += 1
            else: 
                count -= 1
            if count not in table:
                table[count] = i
            else:
                result = max(result, i - table[count])
        return result
