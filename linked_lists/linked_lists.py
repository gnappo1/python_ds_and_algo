#! 1. Complexity Comparison: Linked Lists vs Arrays

# | Operation           | Singly Linked List       | Doubly Linked List       | Array/List       |
# |-------------------------|------------------------------|------------------------------|----------------------|
# | Access (Random)     | O(n)                         | O(n)                        | O(1)                |
# | Search              | O(n)                         | O(n)                        | O(n)                |
# | Insertion (Head)    | O(1)                         | O(1)                        | O(n) (due to shifts) |
# | Insertion (Middle)  | O(n) (traversal)             | O(n)                        | O(n) (due to shifts) |
# | Insertion (End)     | O(n) (traversal)  *          | O(n) **                     | O(1) amortized \\  |
# | Deletion (Head)     | O(1)                         | O(1)                        | O(n) (due to shifts) |
# | Deletion (Middle)   | O(n) (traversal)             | O(n)                        | O(n) (due to shifts) |
# | Deletion (End)      | O(n) (traversal)  *          | O(n) **                     | O(1) amortized \\  |

# Notes:
# - * With a tail pointer, insert/delete at the end is O(1).
# - ** Dynamic arrays occasionally resize, causing an amortized cost of O(n) during resizing.


#! 2. Optimizing Linked Lists for Efficiency

# Linked lists inherently have more overhead compared to arrays, but we can optimize their structure and operations to address some drawbacks:

#a) Tail Pointer for Faster End Operations
# - Add a `tail` pointer to allow O(1) insertions at the end of the list.
# - Similarly, maintain a `size` variable to avoid recomputing the list's length (useful in problems requiring size checks).

#b) Memory Pooling
# - To address memory fragmentation, use a memory pool:
#   - Preallocate memory for nodes and reuse freed-up nodes instead of relying on individual allocations.
#   - This technique reduces the overhead of pointer management.


#! 3. When to Use Linked Lists

#* Ideal Use Cases:
# 1. Dynamic Insertions/Deletions in the Middle of a List
#    - When operations like `insert_after`, `delete_after`, or moving items around are frequent.
#    - Example: Real-time scheduling systems or undo functionality in text editors.

# 2. Constant Add/Remove at the Head
#    - Use a singly linked list if you need constant-time insertion/deletion at the head (e.g., stacks, queues).

# 3. Memory Constrained or Large Elements
#    - When memory fragmentation isn’t a concern, and you're working with large data blocks (e.g., images or objects).

#*Not Ideal For:
# 1. Random Access
#    - Arrays are far superior when you need frequent random access or indexed operations.

# 2. Small Elements
#    - As you pointed out, for small data (e.g., integers), pointer overhead and memory fragmentation make linked lists inefficient.

# 3. Modern CPU Architectures
#    - Arrays benefit significantly from cache locality on modern CPUs, making them faster in practice for many use cases.

#! 4. Drawbacks of Linked Lists in Depth

#a) Cache Locality
# - Arrays shine because their elements are stored in contiguous memory blocks:
#   - Cache lines prefetch adjacent memory, so accessing elements sequentially in an array is almost instant after the first access.
#   - Linked lists, however, jump to random memory locations, missing the cache frequently and resulting in high latency.

# b) Memory Overhead
# - Each node in a singly linked list requires at least 8 bytes (64-bit pointer) for the `next` reference. In doubly linked lists, this overhead doubles to 16 bytes.
# - If the data being stored is small (e.g., 4-byte integers), the overhead can consume up to 80% of the memory.

# c) Memory Fragmentation
# - Linked lists allocate memory individually for each node:
#   - Allocators typically provide memory in fixed blocks, leading to unused space in each block.
#   - This fragmentation worsens as the list grows or shrinks dynamically.

# d) Debugging Complexity
# - Linked lists are more prone to issues like null pointer dereferencing, memory leaks, or dangling pointers compared to arrays.

# e) Poor Real-World Performance
# - Despite theoretically lower complexity for certain operations, the lack of cache efficiency makes linked lists slower in practice for common scenarios.


### 5. Comparing Arrays and Linked Lists in Practice

# | Factor                | Array                       | Linked List                   |
# |---------------------------|----------------------------------|------------------------------------|
# | Cache Efficiency      | High (due to contiguous memory) | Low (random memory access)        |
# | Memory Overhead       | Minimal                        | High (pointers and fragmentation) |
# | Dynamic Resizing       | Costly during resizing         | Efficient for frequent insertions |
# | Ease of Use           | High (index-based operations)  | Low (manual pointer management)   |
# | Real-World Speed      | Generally faster               | Slower in most cases              |


#! Final Takeaway

# - Linked lists are conceptually elegant and great for specific problems requiring dynamic memory allocation or frequent insertions/deletions in the middle.
# - Arrays/lists are the go-to choice for most practical scenarios due to their better real-world performance, cache locality, and lower memory overhead.
  
# For modern systems, optimize linked lists using techniques like tail pointers, memory pooling, or skip lists, but always evaluate if arrays or other dynamic data structures can solve the problem more efficiently.

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