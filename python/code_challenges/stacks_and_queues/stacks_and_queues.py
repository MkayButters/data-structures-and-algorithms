
class Node:

    def __init__(self, value, next_= None):
        self.value = value
        self.next = next_


class InvalidOperationError(Exception):
    pass


class Stack:

    def __init__(self):
        self.top = None


    def push(self, value):

        node = Node(value)
        node.next = self.top
        self.top = node


    def pop(self):

        if self.top:
            value = self.top.value
            self.top = self.top.next
            return value

        raise InvalidOperationError('Method not allowed on empty collection')


    def is_empty(self):

        return not self.top


    def peek(self):

        if self.is_empty():
            raise InvalidOperationError('Method not allowed on empty collection')

        return self.top.value


class Queue:

    def __init__(self):

        self.front = None
        self.back = None
        self.size = 0

    def enqueue(self, value):

        node = Node(value)
        if not self.front:
            self.front = node
            self.back = node
            self.size += 1
            return node
        if value is None:
            raise InvalidOperationError('Node value cannot be none')
        self.back.next = node
        self.back = node
        self.size += 1
        if self.size == 1:
            self.front = node
        return node


    def dequeue(self):
        if self.front == None:
            raise InvalidOperationError('Cannot dequeue from empty queue')
        current_node = self.front
        if self.front:
            self.front = self.front.next
            self.size -= 1
        return str(current_node.value)


    def peek(self):
        if self.front == None:
            raise InvalidOperationError("Method not allowed on empty collection")
        return str(self.front.value)


    def is_empty(self):
        if not self.front:
           return True
        else:
            return False

