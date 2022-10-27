class DetectSquares(object):

    def __init__(self):
        self.d = collections.defaultdict(int)

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        self.d[tuple(point)] += 1
        

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        px,py = point
        res = 0
        for x, y in self.d.keys():
            if (abs(px-x) != abs(py-y)) or px == x or py == y:
                continue
            res += self.d[(x,py)] * self.d[(px,y)]  * self.d[(x,y)]
        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)

# use a dic to keep track the freq of a point
# traverse the points in dic, find the diaganol point in the dic
   # px, py - x,y - abs(py - y) == abs(px - x) and px != x and py!=y
