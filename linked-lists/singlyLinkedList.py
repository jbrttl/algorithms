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
    def __init__(self, node = None):
        self.lenght = 0
        self.head = node

    def __len__(self):
        return len(tuple(item(self)))

    def __repr__(self):
        """Create string representation of Linked List instance."""
        return "->".join([str(item) for item in self])
