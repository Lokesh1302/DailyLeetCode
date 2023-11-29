class Solution:
    def hammingWeight(self, n: int) -> int:
        _sum = 0
        for i in range(32):
            _sum += (n >> i) & 1
        return _sum
