class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()

        left, right = 0, len(tokens) - 1

        max_score = 0
        cur_score = 0

        while left <= right:
            while left <= right and tokens[left] <= power:
                power = power - tokens[left]
                cur_score += 1
                left += 1
            max_score = max(max_score, cur_score)
            if cur_score > 0 and left <= right:
                power = power + tokens[right]
                right -= 1
                cur_score -= 1

            if left <= right and power < tokens[left]:
                break

        return max_score   
