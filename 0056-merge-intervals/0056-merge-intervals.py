class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # care about the end and start relations:
        # if the last end >= the next start, we merge it together 
        intervals.sort()
        output = []
        output.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] <= output[-1][-1]:
                output[-1][-1] = max(intervals[i][1], output[-1][-1])
            else:
                output.append(intervals[i])
        return output
        