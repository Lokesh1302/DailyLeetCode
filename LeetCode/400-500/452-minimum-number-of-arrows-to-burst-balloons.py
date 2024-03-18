class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key =lambda x: x[0])
        merged =[]
        
        for point in points:
            if not merged or merged[-1][-1] < point[0]:
                merged.append(point)
            else:
                merged[-1][1] = min(merged[-1][1], point[1])
                merged[-1][0] = max(merged[-1][0], point[0])

        return len(merged)

# Merge Intervals Problems. See below examples.

#   
#  1---6
#    2 --- 8
#        7 -----12
#           10 --- 16

# 2 -- 6
#        10 -- 12

# 1 -- 2
#      2 -- 3
#           3 -- 4
#                4 -- 5
# [2, 2] [4, 4]
