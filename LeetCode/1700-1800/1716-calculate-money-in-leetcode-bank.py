class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        day = 1
        for i in range(1, n + 1):
            total += day
            day += 1
            if i % 7 == 0:
                day = 1 + i // 7
        return total
