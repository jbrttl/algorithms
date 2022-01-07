class Node:
    """Initiate node instance of a list."""
    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

    def set_data(self,data):
        self.data = data

    def set_next(self, next):
        self.next = next

    def set_previous(self, previous):
        self.previous = previous

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_previous(self):
        return self.previous

    def __repr__(self):
        return f"Node({self.data})"

class circularLinkedList(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insert_head(self, data):
        self.insert_anywhere(0, data)

    def insert_tail(self,data):
        self.insert_anywhere(len(self), data)

    def insert_anywhere(self, position, data):
        if position < 0 or position > len(self):
            raise IndexError('Index out of range.')
        newNode = Node(data)
        if self.head is None:
            newNode.next = newNode
            self.tail = self.head = newNode
        elif position == 0:  # insert at head
            newNode.next = self.head
            self.head = self.tail.next = newNode
        else:
            temp = self.head
            for _ in range(position - 1):
                temp = temp.next
            newNode.next = temp.next
            temp.next = newNode
            if position == len(self) - 1:
                self.tail = newNode

    def __iter__(self):
        """Turn list to an interrator."""
        node = self.head
        while self.head:
            yield node.data
            node = node.next
            if node == self.head:
                break

    def __len__(self):
        """Return lenght of the linked list instance."""
        return len(tuple(iter(self)))

    def __repr__(self):
        """Create string representation of Linked List instance."""
        return " -> ".join([str(item) for item in iter(self)])


if __name__ == '__main__':
    linked_list = circularLinkedList()
    linked_list.insert_head(4)
    linked_list.insert_head('Hi')
    linked_list.insert_head(1000)
    linked_list.insert_head((1000,50))
    print(linked_list)
    linked_list.insert_tail(999)
    linked_list.insert_tail('Some string')
    linked_list.insert_tail('Content')
    print(linked_list)
