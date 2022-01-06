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

    def insert_tail(self, data):
        """Insert new node at the tail of the linked list instance."""
        newNode = Node()
        newNode.data = data
        current = self.head
        while current.next != None:
            current = current.next
        current.next = newNode

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

    def delete_head(self):
        """Delete head of the linked list instance."""
        if len(self) == 0:
            raise ValueError('Empty instance of linked list, nothing to delete.')
        else:
            self.head = self.head.next

    def delete_node(self,node):
        if len(self) == 0:
            raise ValueError('Empty instance of linked list, nothing to delete.')
        else:
            current = self.head
            previous = None
            found = False

            while not found:
                if current.data == node.data:
                    found = True
                elif current is None:
                    raise ValueError('Node not in linked list')
                else:
                    previous = current
                    current = current.next
            if previous is None:
                self.head = current.next
            else:
                previous.next = current.next
                current = current.next

    def delete_node_data(self,data):
        current = self.head
        previous = self.head
        while current.next != None or current.data != data:
            if current.data == data:
                previous.next = current.next
                return
            else:
                previous = current
                current = current.next

    def delete_position(self,position):
        count = 0
        current = self.head
        previous = self.head
        if position > len(self) or position < 0:
            raise ValueError('Position does not exist.')
        else:
            while current.next != None or count < position:
                if count == position:
                    previous.next = current.next
                    return
                else:
                    previous = current
                    current = current.next
                count += 1

    def delete_tail(self):
        """Delete tail of the linked list instance."""
        if len(self) == 0:
            raise ValueError('Empty instance of linked list, nothing to delete.')
        else:
            current = self.head
            previous = self.head

            while current.next != None:
                previous = current
                current = current.next
            previous.next = None

    def delete_instance(self):
        """Delete instance of linked list."""
        self.head = None

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
    linked_list.insert_tail('Hello, hello.')
    linked_list.insert_tail(100)
    linked_list.insert_anywhere('Hi hi', 3)
    linked_list.insert_anywhere('Hoopla', 9)
    linked_list.insert_anywhere(999, 0)
    print(linked_list)
    print(len(linked_list))
    for node in linked_list:
        print(node)

    print('Deleting...')
    print('Before head delete...')
    print(linked_list)
    linked_list.delete_head()
    print('Delete head...')
    print(linked_list)
    linked_list.delete_tail()
    print('Delete tail...')
    print(linked_list)
    linked_list.delete_node(Node(4))
    print('Delete node...')
    print(linked_list)
    print('Deleting data...')
    print('Before data delete...')
    print(linked_list)
    linked_list.delete_node_data('Hi')
    print('After data delete...')
    print(linked_list)
    print('Deleting at position...')
    print('Before position delete...')
    print(linked_list)
    linked_list.delete_position(1)
    print('After position delete...')
    print(linked_list)
    print('Delete instance...')
    linked_list.delete_instance()
    print(f'Empty instance: {linked_list}, Number of items: {len(linked_list)}')
