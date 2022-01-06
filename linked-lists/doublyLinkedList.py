#Doubly linked list

class Node:
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

class DoublyLinkedList(object):

    def __init__(self, head=None, next=None):
        self.head = head

    def insert_head(self, data):
        self.insert_anywhere(0, data)

    def insert_tail(self,data):
        self.insert_anywhere(len(self), data)

    def insert_anywhere(self, position, data):
        if not 0 <= position <= len(self):
            raise IndexError('Index out of range.')
        newNode = Node(data)
        if self.head is None:
            self.head = self.tail = newNode
        elif position == 0:
            self.head.previous = newNode
            newNode.next = self.head
            self.head = newNode
        else:
            temp = self.head
            for i in range(0,position-1):
                temp = temp.next
            newNode.previous = temp
            temp.next = newNode
            newNode.next = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __len__(self):
        """Return lenght of the linked list instance."""
        return len(tuple(iter(self)))

    def __repr__(self):
        """Create string representation of Linked List instance."""
        current = self.head
        items = list()
        while current != None:
            items.append(current)
            current = current.next
        return " -> ".join([str(item.data) for item in items])

if __name__ == '__main__':
    linked_list = DoublyLinkedList()
    linked_list.insert_head(4)
    linked_list.insert_head('Hi')
    linked_list.insert_head('Hello ,hello')
    linked_list.insert_tail({'1':'content'})
    linked_list.insert_tail((4,5))
    linked_list.insert_tail(100)
    print(linked_list)
    for i in linked_list:
         print(i)
