from python_linked_list import LinkedList

def test_if_new_list_is_empty():
    new_linked_list = LinkedList()
    assert new_linked_list.head is None

def test_if_first_append_value_is_assigned_as_head():
    new_linked_list = LinkedList()
    new_linked_list.append(10)
    new_linked_list.append(40)
    assert new_linked_list.head.value == 10

def test_check_str_representation_of_linked_list():
    new_linked_list = LinkedList()
    new_linked_list.append(10)
    new_linked_list.append(40)
    new_linked_list.append(99)
    assert str(new_linked_list) == "[10 -> 40 -> 99]"

def test_if_pop_returns_none_when_empty():
    new_linked_list = LinkedList()
    assert new_linked_list.pop() is None

def test_if_pop_returns_last_element_when_non_empty():
    new_linked_list = LinkedList()
    new_linked_list.append(19)
    new_linked_list.append(20)
    new_linked_list.append(45)
    assert new_linked_list.pop() == 45

def test_if_pop_empties_the_list_with_only_head_element():
    new_linked_list = LinkedList()
    new_linked_list.append(19)
    new_linked_list.pop()
    assert new_linked_list.head is None

# NOTE: 
# To run the test:
#  1. open terminal.
#  2. cd to the path of test_python_linked_list.py 
#  3. type pytest and press enter.