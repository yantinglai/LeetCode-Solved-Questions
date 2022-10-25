import heapq 
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # sort the intervals 
        # use a heap to store the room, with the end time
        # compare the next start time with the minimum end time
        # if it is bigger, put the new end time in the heap, pop it out
        # if it is not bigger, it means there is collision, put it in heap
        intervals.sort()
        q =[]
        heapq.heappush(q, intervals[0][1])
        
        for i in range(1, len(intervals)):
            if intervals[i][0] >= q[0]:
                heapq.heappop(q)
                heapq.heappush(q, intervals[i][1])
            else:
                heapq.heappush(q, intervals[i][1])
        return len(q)
            
            