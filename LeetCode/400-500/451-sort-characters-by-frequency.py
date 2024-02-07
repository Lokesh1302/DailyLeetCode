import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for i in s:
            if i not in freq:
                freq[i] = 0
            freq[i] += 1
        heap = [(-value, key) for key, value in freq.items()]
        heapq.heapify(heap)
        result = ''
        while heap:
            value, key = heapq.heappop(heap)
            value = value * -1
            result += key * value
        return result
