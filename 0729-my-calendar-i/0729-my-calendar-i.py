class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        if len(self.calendar) < 1: 
            self.calendar.append([start,end])
            return True
        
        for i in range(len(self.calendar)):
            if self.calendar[i][0] >= end or self.calendar[i][1] <= start:
                continue
            else:
                return False
        self.calendar.append([start,end])
        return True
            
    # 解题思路：
    # # 遍历res 里面的所有元素，一个一个的和 当前的 start, end 进行比较
    # 能够插入的条件是：所有的元素和我这个start以及end都没有交集的时候，把所有元素遍历完之后，append -      return True
    # 一旦发现有交集，return false
                
            


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)