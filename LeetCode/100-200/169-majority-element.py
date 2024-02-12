class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = len(nums) // 2
        freq = {}
        for cur in nums:
            if cur not in freq:
                freq[cur] = 0
            freq[cur] += 1
            if freq[cur] > target:
                return cur
        return -1
