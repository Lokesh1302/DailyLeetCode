class Solution:
    def largestGoodInteger(self, num: str) -> str:
        cur_max = ''
        for index in range(2, len(num)):
            if num[index] == num[index - 1] and num[index - 1] == num[index - 2]:
                if cur_max == '' or cur_max < num[index]:
                    cur_max = num[index]
        return cur_max + cur_max + cur_max
