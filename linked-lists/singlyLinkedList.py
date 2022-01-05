#Singly linked lists

class Node:
    """Create and initialize Node class instance."""
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

    def set_data(self,data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self,next):
        self.next = next

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next != None

    def __repr__(self):
        """Create string representation of Node instance."""
        return f"Node({self.data})"

class LinkedList(object):
    """Create and initialize an instance of linked list."""
    def __init__(self, node = None):
        self.length = 0
        self.head = node

    def insert_head(self, data):
        """Insert new node at the head of the linked list instance."""
        newNode= Node()
        newNode.data = data
        if self.head == 0:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def insert_tail(self, data):
        """Insert new node at the tail of the linked list instance."""
        newNode = Node()
        newNode.data = data
        current = self.head
        while current.next != None:
            current = current.next
        current.next = newNode
        self.length += 1

    def insert_anywhere(self, data, position):
        if position > len(self) or position < 0:
            return None
        else:
            if position == 0:
                self.insert_head(data)
            else:
                newNode = Node()
                newNode.data = data
                count = 1
                current = self.head
                while count < position-1:
                    count += 1
                    current = current.next
                newNode.next = current.next
                current.next = newNode
                self.length += 1

    def delete_head(self):
        """Delete head of the linked list instance."""
        if self.length == 0:
            print('Empty instance of linked list, nothing to delete.')
        else:
            self.head == self.head.next
            self.length -= 1

    def __iter__(self):
        """
        Make Linked List an iterrator.
        linked_list = LinkedList()
        linked_list.insert_head(4)
        linked_list.insert_head('Hi.')
        for node in linked_list:
            node
        """
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
        return "->".join([str(item.data) for item in items])


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_head(4)
    linked_list.insert_head('Hi')
    linked_list.insert_head((5,6))
    print(linked_list)
    linked_list.insert_tail('Hello, hello.')
    linked_list.insert_tail(100)
    print(linked_list)
    linked_list.insert_anywhere('Hi hi', 3)
    linked_list.insert_anywhere('Hoopla', 9)
    linked_list.insert_anywhere(999, 0)
    print(linked_list)
    print(len(linked_list))
    for node in linked_list:
        print(node)
