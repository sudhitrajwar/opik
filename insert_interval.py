class Solution:
    def insert(self, intervals, newInterval):
        res = []
        for i in range(len(intervals)):
            # Case 1: interval completely before newInterval
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            # Case 2: interval completely after newInterval
            elif intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]  # add rest and return
            # Case 3: overlap — merge intervals
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        
        # if newInterval is last
        res.append(newInterval)
        return res
