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
            
                
            


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)