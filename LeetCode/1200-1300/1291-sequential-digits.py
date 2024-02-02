class Solution:
    def numOfDigits(self, num: int):
        count = 0
        while(num != 0):
            num = num//10
            count += 1
        return count
    
    def generate(self, digits: int):
        count = 0
        for i in range(digits):
            count = count * 10 + 1
        return count

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        first, result = 0, []
        low_digits = self.numOfDigits(low)
        high_digits = self.numOfDigits(high)

        for i in range(low_digits):
            first += self.generate(i)

        for i in range(low_digits, high_digits + 1):
            increment = self.generate(i)
            prev = first
            first = first + increment
            for j in range(1, 9 - i + 2):
                prev = prev + increment
                if low <= prev and prev <= high:
                    result.append(prev)
        return result
