from node import Node

class Linkedlist:
    def __init__(self, node=None):
        # if not isinstance(node, Node):
        #     raise TypeError("node parameter requires 'Node' type.")
        self.length = 0
        self.head = node

    def list_length(self):
        if self.length == 0:
            print("List is empty")
            return 0
        current = self.head
        count = 1
        while current.next != None:
            count += 1
            current = current.get_next()
        return count
    
    def insertion(self, value, pos=None):
        # pos is zero-indexed based
        new_node = Node(value)
        current = self.head
        if pos is None:
            pos = self.length
        if pos < 0 or pos > self.length:
            print("Invalid position provided.")
            return
        if pos == 0:
                new_node.set_next(self.head)
                self.head = new_node
                self.length += 1
        else : 
            if pos == self.length:
                while current.next != None:
                    current = current.get_next()
                current.set_next(new_node)
                self.length += 1
            else:
                count = 1
                while count < pos-1:
                    count += 1
                    current = current.get_next()
                new_node.set_next(current.next)
                current.set_next(new_node)
                self.length += 1
