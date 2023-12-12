class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        freq = defaultdict(int)
        for i in arr:
            freq[i] += 1
        
        result = 0
        count = len(arr)/4
        for key, val in freq.items():
            if val > count:
                return key
        return result
