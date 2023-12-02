class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq = {}
        for cur_char in chars:
            if cur_char not in freq:
                freq[cur_char] = 0
            freq[cur_char] += 1
        
        result = 0

        for word in words:
            cur_freq = {}
            cur_result = len(word)
            for cur_char in word:
                if cur_char not in cur_freq:
                    cur_freq[cur_char] = 0
                cur_freq[cur_char] += 1
            for key, value in cur_freq.items():
                if key not in freq or freq[key] < value:
                    cur_result = 0
                    break
            result += cur_result
        return result
