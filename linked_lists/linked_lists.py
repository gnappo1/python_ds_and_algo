class ListNode(object):
    def __init__(self, value:any=0, next:'ListNode'=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head: ListNode = None
        self.tail: ListNode = None
        self.size: int = 0

    def __len__(self):
        """Return the number of elements in the linked list."""
        return self.size

    def is_empty(self) -> bool:
        """Return True if the linked list is empty, False otherwise."""
        return self.size == 0

    def append(self, value: any):
        """Insert a new element at the end of the linked list."""
        new_node = ListNode(value)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def prepend(self, value: any):
        """Insert a new element at the start of the linked list."""
        new_node = ListNode(value, next=self.head)
        if self.is_empty():
            self.tail = new_node
        self.head = new_node
        self.size += 1

    def delete(self, value: any) -> bool:
        """Delete the first occurrence of the value in the linked list."""
        if self.is_empty():
            return False

        # Special case: Deleting the head
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.size -= 1
            return True

        # General case, traverse to find the node to delete
        current = self.head
        while current.next and current.next.value != value:
            current = current.next

        if current.next:  # Node found
            current.next = current.next.next
            if current.next is None:  # If we deleted the tail
                self.tail = current
            self.size -= 1
            return True

        return False

    def search(self, value: any) -> bool:
        """Return True if the value is found in the linked list, False otherwise."""
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def reverse(self):
        """Reverse the linked list in place."""
        prev = None
        current = self.head
        self.tail = self.head  # Update the tail to the original head
        while current:
            next_node = current.next  # Store the next node
            current.next = prev  # Reverse the pointer
            prev = current  # Move prev forward
            current = next_node  # Move current forward
        self.head = prev  # Update the head to the last node

    def to_list(self) -> list:
        """Convert the linked list to a Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def __repr__(self):
        """String representation of the linked list."""
        nodes = []
        current = self.head
        while current:
            nodes.append(repr(current.value))
            current = current.next
        return " -> ".join(nodes)

# Test everything
ll = LinkedList()
print(ll)
print(ll.is_empty())
ll.append(1)
ll.append(2)
ll.append(3)
print(ll)
print(ll.is_empty())
ll.prepend(0)
print(ll)
print(ll.search(1))
print(ll.search(4))
ll.reverse()
print(ll)