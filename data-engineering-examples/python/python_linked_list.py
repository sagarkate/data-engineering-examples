class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head
    
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)

    def pop(self):
        '''
        return the last node value of the linked list by removing that node
        '''
        if self.head is None:
            return None
        elif self.head.next is None:
            popped_value = self.head.value
            self.head = None
            return popped_value
        else:
            current_node = self.head
            while current_node.next.next is not None:
                current_node = current_node.next
            popped_value = current_node.next.value
            current_node.next = None
            return popped_value

    def peek(self):
        '''
        return the last node value of the linked list without removing that node
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
        remove the last node value of the linked list
        '''
        if self.head is None:
            return None
        elif self.head.next is None:
            self.head = None
            return None
        else:
            current_node = self.head
            while current_node.next.next is not None:
                current_node = current_node.next
            current_node.next = None
            return None

    def insert_at_start(self, value):
        '''
        add a new node at the start of the linked list
        '''
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = Node(value)
            current_node.next = self.head
            self.head = current_node

    def remove_from_first(self):
        '''
        remove node from the start of the linked list
        '''
        if self.head is None:
            return None
        else:
            self.head = self.head.next
        
    def __str__(self) -> str:
        if self.head is None:
            return "[]"
        else:
            linked_list = []
            current_node = self.head
            while current_node.next is not None:
                linked_list.append(f"{current_node.value}")
                current_node = current_node.next
            linked_list.append(f"{current_node.value}")
            return " -> ".join(linked_list)

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
    my_linked_list.remove_from_first()
    print(f"\nmy_linked_list after using remove_from_first(): {my_linked_list}")

if __name__ == "__main__":
    main()
