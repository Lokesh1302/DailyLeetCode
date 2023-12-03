class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        distance = 0
        for cur_index in range(1, len(points)):
            prev = points[cur_index - 1]
            cur = points[cur_index]
            distance += max(abs(cur[0] - prev[0]), abs(cur[1] - prev[1]))
        return distance            
