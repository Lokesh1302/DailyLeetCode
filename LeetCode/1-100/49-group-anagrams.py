class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for i in strs:
            key = ''.join(sorted(i))
            if key not in result:
                result[key] = []
            result[key].append(i) 
        return result.values()
