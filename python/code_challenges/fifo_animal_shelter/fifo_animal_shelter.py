class Node:

    def __init__(self, value, next_= None):
        self.value = value
        self.next = next_


class InvalidOperationError(Exception):
    pass


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


class AnimalShelter:

    def __init__(self):

        self.cat_queue = Queue()
        self.dog_queue = Queue()


    def enqueue(self, animal):

        if animal == "cat":
            self.cat_queue.enqueue(animal)
        elif animal == "dog":
            self.dog_queue.enqueue(animal)
        else:
            raise InvalidOperationError("This is not a dog or a cat")


    def dequeue(self, pref):

        if pref == "dog":
           selected_dog = self.dog_queue.dequeue()
           return selected_dog
        if pref == "cat":
            selected_cat = self.cat_queue.dequeue()
            return selected_cat
        else:
            raise InvalidOperationError("This is not a dog or a cat")
