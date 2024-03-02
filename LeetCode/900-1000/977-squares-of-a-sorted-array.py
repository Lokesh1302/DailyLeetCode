# Time Complexity : O(N)
# Space Complexity : O(1) # we can modify the result array if space is a problem.
# Approach : We can start at both the end and compare absolute values and add the result to and keep moving left or right.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start, end = 0, len(nums) - 1
        index = end
        result = [0] * len(nums) 

        while start <= end:
            if abs(nums[end]) > abs(nums[start]):
                cur = nums[end] * nums[end]
                end -= 1
            else:
                cur = nums[start] * nums[start]
                start += 1
            result[index] = cur
            index -= 1
        return result




    # def sortedSquares(self, nums: List[int]) -> List[int]:
    #     start = 0
    #     min_val = float("inf")
    #     size = len(nums)
    #     for index in range(size):
    #         if abs(nums[index]) < min_val:
    #             min_val = abs(nums[index])
    #             start = index

    #     left, right = start - 1, start + 1
    #     result = [nums[start]*nums[start]]

    #     while left >= 0 and right < size:
    #         if abs(nums[left]) < abs(nums[right]):
    #             cur = nums[left] * nums[left]
    #             left -= 1
    #         else:
    #             cur = nums[right] * nums[right]
    #             right += 1               
    #         result.append(cur)
        
    #     while left >= 0:
    #         cur = nums[left] * nums[left]
    #         left -= 1
    #         result.append(cur)

    #     while right < size:
    #         cur = nums[right] * nums[right]
    #         right += 1
    #         result.append(cur)
                
    #     return result
