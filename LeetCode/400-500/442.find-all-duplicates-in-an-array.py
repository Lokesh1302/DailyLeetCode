class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq = {}
        result = set()
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] > 1:
                result.add(num)
        return list(result)
