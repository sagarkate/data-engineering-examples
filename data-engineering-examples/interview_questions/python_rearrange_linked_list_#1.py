# Problem Statement:
# Rearrange Linked List in such a way that all the even indexed nodes
# will appear after all the odd indexed nodes

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    
    def __repr__(self) -> str:
        return f"Node[{self.value}]"

# Modified LinkedList implementation to add tail node 
# to avoid iterating the entire linked list to extend it by another linked list.

class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head
        self.tail = head
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
            self.tail = self.head
        else:
            current_node = Node(value)
            self.tail.next = current_node
            self.tail = current_node
        self.size += 1
        # print(self.tail) # Debug

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
            self.tail = None
            self.size -= 1
            return popped_value
        else:
            current_node = self.head
            while current_node.next.next is not None:
                current_node = current_node.next
            popped_value = current_node.next.value
            current_node.next = None
            self.tail = current_node
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
            return self.tail.value

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
            self.tail = current_node
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
            self.tail = self.head
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
            if self.head is None:
                self.tail = None
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
    
    def __repr__(self) -> str:
        return str(self)
        
    def __len__(self):
        return self.size

def rearrange_linked_list(input_linked_list: LinkedList) -> LinkedList:
    length_of_linked_list = len(input_linked_list)
    if length_of_linked_list <= 1:
        return input_linked_list
    else:
        current_node = input_linked_list.head
        odd_indexed_nodes = LinkedList()
        even_indexed_nodes = LinkedList() # I am creating a separate even nodes list to avoid modifying existing list
        for index in range(length_of_linked_list-1):
            if index % 2 == 0:
                even_indexed_nodes.append(current_node.value)
            else:
                odd_indexed_nodes.append(current_node.value)
            current_node = current_node.next
        
        if (index + 1) % 2 == 0:
            even_indexed_nodes.append(current_node.value)
        else:
            odd_indexed_nodes.append(current_node.value)
        
        odd_indexed_nodes.tail.next = even_indexed_nodes.head
        return odd_indexed_nodes

def main():
    my_linked_list = LinkedList()
    my_linked_list.append(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(4)
    my_linked_list.append(5)
    my_linked_list.append(6)
    my_linked_list.append(7)
    my_linked_list.append(8)
    my_linked_list.append(9)
    my_linked_list.append(10)
    print(f"my_linked_list: {my_linked_list}")
    rearranged_linked_list = rearrange_linked_list(my_linked_list)
    print(f"rearranged_linked_list: {rearranged_linked_list}")

if __name__ == "__main__":
    main()
