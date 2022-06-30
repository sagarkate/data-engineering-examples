'''
This Program has 2 classes: Node and LinkedList
    Node:
        -   This is the node of a linked list.
        -   It holds value of the current node and,
            reference to the next node in the list.
    
    LinkedList:
        -   This is the implementation of Linked List.
        -   We can create the empty linked list or,
            we could pass in the head node while creating
            a new linked list.
        -   We have below methods available:
                - append(value)
                - pop()
                - peek()
                - remove()
                - insert_at_start(value)
                - remove_from_start()
'''

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head
        if self.head is None:
            self.size = 0
        else:
            self.size = 1
    
    def append(self, value):
        '''
        -   Add a new node to the linked list.
        -   If the linked list is empty, create a new node and make it head of the linked list.
        -   If the linked list is not empty, traverse to the end of the linked list and add a new node at the end.
        '''
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)
        self.size += 1

    def pop(self):
        '''
        -   Return the value of last node of the linked list by removing that node.
        -   If the linked list is empty, return None.
        -   If the linked list has only head node, remove that node, mark the linked list as empty and, 
            return the value of the head node.
        -   If the linked list has more nodes apart from the head, traverse to the penultimate node 
            of the linked list. Remove its next node (i.e. the last node) and return the value of the last node.
        '''
        if self.head is None:
            return None
        elif self.head.next is None:
            popped_value = self.head.value
            self.head = None
            self.size -= 1
            return popped_value
        else:
            current_node = self.head
            while current_node.next.next is not None:
                current_node = current_node.next
            popped_value = current_node.next.value
            current_node.next = None
            self.size -= 1
            return popped_value

    def peek(self):
        '''
        -   Return the value of the last node of the linked list without removing that node.
        -   If the linked list is empty, return None.
        '''
        if self.head is None:
            return None
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            return current_node.value

    def remove(self):
        '''
        -   Remove the last node of the linked list.
        -   If the linked list is empty, do nothing.
        -   If the linked list has only head node, mark it as None, making the linked list empty.
        -   If the linked list has more nodes other than the head node, traverse to the 
            penultimate node of the linked list and mark its next node as None.
        '''
        if self.head is None:
            return None
        elif self.head.next is None:
            self.head = None
            self.size -= 1
            return None
        else:
            current_node = self.head
            while current_node.next.next is not None:
                current_node = current_node.next
            current_node.next = None
            self.size -= 1
            return None

    def insert_at_start(self, value):
        '''
        -   Add a new node at the start of the linked list.
        -   If the linked list is empty, create a new node and mark it as the head of the linked list.
        -   If the linked list is not empty, create a new node, assign head node as its next node and,
            mark the new node as the new head of the linked list.
        '''
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = Node(value)
            current_node.next = self.head
            self.head = current_node
        self.size += 1

    def remove_from_start(self):
        '''
        -   Remove a node from the start of the linked list.
        -   If the linked list is empty, do nothing.
        -   If the list is not empty, mark the next node of the head node as the new head of the linked list.
        '''
        if self.head is None:
            return None
        else:
            self.head = self.head.next
        self.size -= 1
        
    def __str__(self) -> str:
        '''
        -   Return the linked list in string format like [10 -> 20 -> 30]
        -   If the linked list is empty, return []
        '''
        if self.head is None:
            return "[]"
        else:
            linked_list = []
            current_node = self.head
            while current_node.next is not None:
                linked_list.append(f"{current_node.value}")
                current_node = current_node.next
            linked_list.append(f"{current_node.value}")
            return "[" + " -> ".join(linked_list) + "]"
        
    def __len__(self):
        return self.size

def main():
    my_linked_list = LinkedList()
    my_linked_list.append(10)
    my_linked_list.append(20)
    my_linked_list.append(12)
    my_linked_list.append(90)
    my_linked_list.append(36)

    print(f"Initial my_linked_list: {my_linked_list}")
    print(f"\nPopped last value: {my_linked_list.pop()}")
    print(f"\nmy_linked_list after 1st pop: {my_linked_list}")
    print(f"\nPeeking at the last value of my_linked_list: {my_linked_list.peek()}")
    print(f"\nmy_linked_list after peek: {my_linked_list}")
    my_linked_list.remove()
    print(f"\nmy_linked_list after 1st remove: {my_linked_list}")
    my_linked_list.insert_at_start(1020)
    print(f"\nmy_linked_list after using insert_at_first(1020): {my_linked_list}")
    my_linked_list.remove_from_start()
    print(f"\nmy_linked_list after using remove_from_start(): {my_linked_list}")

    print(f"Length of my_linked_list: {len(my_linked_list)}")

if __name__ == "__main__":
    main()
