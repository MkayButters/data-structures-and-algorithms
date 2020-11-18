class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return f"{self.value}"

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
        current = self.head
        if not current:
            return "error not found"

        if current.value == value:
            self.insert(newValue)

        if current.value == newValue:
            new_node == (newValue, current)
            self.head = new_node

        else:
            while current.next:
                if current.next.value == value:
                    new_node = Node(newValue, current.next)
                    current.next = new_node
                    break
                current = current.next

    def insertAfter(self, value, newValue):
        if not self.head:
            return "error"

        current = self.head
        while current:
            if current.value == value:
                current.next = Node(newValue, current.next)
                return
            current = current.next

    def k_fromthe_end(self, k):
        counter = 0
        leader = self.head
        follower = self.head
        if k < 0:
            raise ValueError("You cannot enter a negative integer")
        while counter <= k and leader:
            leader = leader.next
            counter += 1
        while leader:
            leader = leader.next
            follower = follower.next
            counter +=1
        if k > counter:
            raise IndexError("The list is not that big")
        return follower.value





