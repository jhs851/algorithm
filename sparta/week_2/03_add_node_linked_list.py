class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur = self.head
        for i in range(index):
            cur = cur.next

        return cur

    def add_node(self, index, value):
        new_node = Node(value)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        node = self.get_node(index - 1)
        new_node.next = node.next
        node.next = new_node


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
# [5] -> [12] -> [8]

# [5] -> [6] -> [12] -> [8]
linked_list.add_node(1, 6)
# linked_list.print_all()

# [7] -> [5] -> [6] -> [12] -> [8]
linked_list.add_node(0, 7)
linked_list.print_all()
