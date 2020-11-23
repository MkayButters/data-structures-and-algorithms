
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

    def __init__(self, front = None):

        self.front = front

    def enqueue(self, value):

        node = Node(value)
        front.next = node
        self.rear = node


    def dequeue(self):
        pass


    def peek(self):
        pass


    def isEmpty(self):
        pass
