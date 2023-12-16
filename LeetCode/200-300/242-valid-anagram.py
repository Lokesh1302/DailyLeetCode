class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for i in s:
            if i not in freq:
                freq[i] = 0
            freq[i] += 1

        for i in t:
            if i not in freq:
                return False
            freq[i] -= 1
        
        for i in freq.values():
            if i != 0:
                return False
        return True
