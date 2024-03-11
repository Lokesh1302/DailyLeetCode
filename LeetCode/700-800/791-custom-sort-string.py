class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = {}
        for cur in s:
            freq[cur] = freq.get(cur, 0) + 1

        result = []
        for cur in order:
            if cur in freq:
                cur_str = [cur] * freq[cur]
                result.append(''.join(cur_str))
                freq[cur] = 0
        
        for key, val in freq.items():
            if val != 0:
                cur_str = [key] * val
                result.append(''.join(cur_str))
        
        return ''.join(result)
            
        
