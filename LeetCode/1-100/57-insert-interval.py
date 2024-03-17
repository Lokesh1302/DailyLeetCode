class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            #non overlaping, new interval is smaller
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res+intervals[i:]
            #non overlapping, new interval is greater, now insert the smaller into res and keep looping
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            #overlapping -- merge the interval and keep looping
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), 
                                max(intervals[i][1], newInterval[1])]
        res.append(newInterval)
        return res
        


#   1 - - - 5
#     2 - 4 Complete Overlap
#   1 - - - 5    
#     2 - - - 6 Start is between the window
#   1 - - - 5   
# 0 - - - 4     End is between the window     
#   1 - - - 5
#             6 - - 8 No overlap
