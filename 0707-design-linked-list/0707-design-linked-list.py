
# 创建单向链表，使用虚拟头节点的时候，有哪些需要注意的事项？
# get index：
# 1. 首先对index进行判断，如果 <0 或者 >= self.count 说明已经越界，直接返回 -1 
# 2. 其次是遍历到index当前所在的位置。因为有虚拟头节点，所以设立cur指针在 self.head, for loop 从(0,index+1 )
# 3. cur 指针停止的地方，就是当前index所在的位置

# add at Index:
# 1. 先对index的界限进行判断，如果 index <0, 重置为0，如果index >= self.count，说明越界，返回-1
# 2. 在当前index的前面插入一个数，说明要遍历到当前index前一位的数字：
# 3. 创建for loop (0,index) - 指针设置为 pre，pre 停下来的位置就是插入index的前一位
# 4. 创建new node，1. new_node.next = pre.next 2. pre.next = new_node 
# 5. 记得要对 self.size += 1 !!!


# 总结：这个链表题最容易出现的bug在哪里
# 1. 如果是get index，一旦 index = self.count 说明 index 已经越界了，要返回 -1
# 2. 如果是 add index，在当前index前面一个node插入元素，那么及时 index = self.count 也是可以符合条件的情况，因为index -1 并没有越界！

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
        if index < 0 or index >= self.count: # 为什么get 这里 index = self.count 也是错的？因为 index = self.count 的时候，已经越界了！
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
         # Add at index 6 -- 如果index == self.count 是什么样的情况？
        # (0) - 6 - 8 - 9 - 3 - 4 - 6  add at index 6, 就在6后面append
        # cur should move 5 steps, so the for loop should be (0, index)
        
        # Add at index 2 -- 如果index < self.count 是什么样的情况？
        # (0) - 6 - 8 - 9 - 3 - 4 - 6  add at index 2, 就在9前面插入元素
        # cur should move 2 steps, so the for loop should be (0, index)
        
        
        # 在尾部添加元素的时候很有可能出错！！！ 为什么这里不能取等号？因为 index == self.count 的时候，指针其实能够遍历到 index-1，即链表的尾巴
        # 所以还是可以成功添加元素的！！！
        if index > self.count: # 这里还包含了一种情况，就是index equals to the length of the linked list!
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