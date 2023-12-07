class Solution:
    def largestOddNumber(self, num: str) -> str:
        str_len = len(num) - 1
        for i in range(str_len, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[0 : i + 1] 
        return ""
