from linked_list.linked_list import LinkedList, Node

def zip_lists(list1, list2):
    if type(list1) != LinkedList or type(list2) != LinkedList:
        raise TypeError('One of the arguments was of not type linked list')

    current_1 = list1.head
    current_2 = list2.head
    while current_1 and current_2:
        temp_1 = current_1.next
        temp_2 = current_2.next
        current_1.next = current_2
        current_2.next = temp_1
        current_1 = temp_1
        current_2 = temp_2
    return list1.head
