class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def insert(self, value):
        new_node = Node(value, self.head)
        self.head = new_node

    def includes(self, value):
        node = self.head
        while node != None:
            if node.value == value:
                return True
            node = node.next
        return False

    def __str__(self):
        node = self.head
        results =  []
        while node != None:
            results.append('{ ' + str(node.value) + ' }')
            node = node.next
        results.append("NULL")
        return " -> ".join(results)

    def append(self, value):
        if self.head == None:
            self.insert(value)
        else:
            current = self.head
            while current.next != None:
                current = current.next

            current.next = Node(value, None)

    def insertBefore(self, value, newValue):
        pass
        # current = self.head
        # if current.next.value == newValue:

    def insertAfter(self, value, newValue):
        pass

