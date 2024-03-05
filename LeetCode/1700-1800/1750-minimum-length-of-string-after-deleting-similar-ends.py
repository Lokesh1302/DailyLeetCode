# class Solution:
#     def minimumLength(self, s: str) -> int:
#         left, right = 0, len(s) - 1
#         size = len(s) - 1

#         while left < right:
#             if s[left] == s[right]:
#                 cur = s[left]
#                 while left <= size and s[left] == cur:
#                     left += 1
                
#                 while right >= 0 and s[right] == cur:
#                     right -= 1
#             else:
#                 break
#             if left > right:
#                 return 0
#         return right - left + 1
             

class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        size = len(s) - 1

        while left < right and s[left] == s[right]:
                cur = s[left]
                
                while left <= right and s[left] == cur:
                    left += 1
                
                while right > left and s[right] == cur:
                    right -= 1

        return right - left + 1

# Cleaner way of doing things.
