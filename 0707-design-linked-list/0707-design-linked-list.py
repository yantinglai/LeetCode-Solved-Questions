class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = Node(0)
        self.count = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.count: 
            return -1
        else:
            cur = self.head
            for _ in range(index+1): # +1 因为算上了 dummy head
                cur = cur.next
            return cur.val
        # (0) - 6 - 8 - 9 - 3 - 4 - 6  get index 4 (should return 4)
        # cur should move 5 steps, so the for loop should be (0, index+1)
    
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.count, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.count: 
            return -1
        if index < 0: 
            index = 0
        cur = self.head
        for _ in range(index):
            cur = cur.next 
        new_node = Node(val)
        new_node.next = cur.next # should first connect new node to cur.next, then connect cur.next to new_node
        cur.next = new_node   # because if you do it reversely, cur.next's address will be lost
    
        self.count += 1
        
        # (0) - 6 - 8 - 9 - 3 - 4 - 6  add at index 4
        # should stop one node before, namely, index 3
        # hence, we don't need to increment the index
        # for loop should be (0, index)
        # increament self.count by 1
            

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.count: return
        else:
            pre = self.head
            for _ in range(index):
                pre = pre.next
            pre.next = pre.next.next
            self.count -= 1




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)