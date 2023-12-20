class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        for i in range(len(prices)):
            if prices[i] >= money: 
                return money
            target = money - prices[i]
            for j in range(i + 1, len(prices)):
                if prices[j] <= target:
                    return target - prices[j]
        return money
