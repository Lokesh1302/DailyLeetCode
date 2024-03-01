class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count1 = -1
        for cur in s:
            if cur == '1':
                count1 += 1

        l1 = ['1'] * count1
        count1 = len(s) - count1 - 1
        for index in range(count1):
            l1.append('0')
        l1.append('1')

        return ''.join(l1)
