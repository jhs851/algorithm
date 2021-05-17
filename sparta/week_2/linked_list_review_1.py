class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        cur = self.head

        while cur.next is not None:
            cur = cur.next

        cur.next = Node(data)

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

    def add_node(self, index, data):
        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        node = self.get_node(index - 1)
        new_node.next = node.next
        node.next = new_node

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return

        node = self.get_node(index - 1)
        node.next = node.next.next


linked_list = LinkedList(6)
linked_list.append(12)
linked_list.append(5)
linked_list.append(7)
linked_list.append(11)

linked_list.add_node(0, 10)
linked_list.add_node(5, 8)

linked_list.delete_node(0)
linked_list.delete_node(4)
linked_list.print_all()
