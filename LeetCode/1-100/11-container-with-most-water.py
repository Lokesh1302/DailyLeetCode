class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1
        while(left < right):
            cur_area = min(height[left], height[right]) * (right - left)
            max_area = max(cur_area, max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
            
