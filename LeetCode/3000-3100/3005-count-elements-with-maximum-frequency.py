class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}
        max_freq = -1
        for cur in nums:
            freq[cur] = freq.get(cur, 0) + 1
            max_freq = max(freq[cur], max_freq)
        
        result = []
        for key, val in freq.items():
            if val == max_freq:
                result.append(key)
        return len(result) * max_freq
