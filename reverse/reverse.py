class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, poorly_structured_unitest):
        curr = node
        prev = None
        while curr:
            nn = curr.next_node
            curr.next_node = prev
            prev = curr
            curr = nn
        self.head = prev


        # if node or node.next_node == None:
        #     return node
        # remaining = self.reverse_list(node.next_node, None)
        # node.next_node.next_node = node
        # node.next_node = None
        # return remaining
