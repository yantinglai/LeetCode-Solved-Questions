class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList(object):

    def __init__(self):
        self.head = Node(0)
        self.size = 0
        

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        # (0) - 4 - 5 - 4 - 7 - 8 - 9  index = 0 - 4  index = 2, 4
        # 0-index+1 
        # index is valid
        if index < 0 or index >= self.size: return - 1
        else:
            cur = self.head
            for _ in range(index+1):
                cur = cur.next 
            return cur.val 
        
    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0,val)
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        # check if index is valid -- 
        # index = self.size
        # if > length, not be inserted 
        # index < 0, append it to the head 
        # [0,self.size]
        if index > self.size: return -1
        if index < 0: 
            index = 0
        # index between 0 and self.size 
        # (0) - 4 - 5 - 4 - 7 - 8 - 9  index = 2 
        self.size += 1
        cur = self.head
        for _ in range(index):
            cur = cur.next
        new_node = Node(val)
        new_node.next = cur.next 
        cur.next = new_node
        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size: return -1 
        #  (0) - 4 - 5 - 4 - 7 - 8 - 9  index = 4
        
        else: 
            pre = self.head
            for _ in range(index):
                pre = pre.next 
            pre.next = pre.next.next 
            self.size -= 1
        
    


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)