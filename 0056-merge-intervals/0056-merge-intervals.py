class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        res = []
        for start, end in intervals:
            if res and start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])
        return res