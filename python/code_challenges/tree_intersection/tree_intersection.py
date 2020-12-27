from .stacks_and_queues import Queue

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self):
        self.root = None

    def pre_order(self):

        values = []

        def walk(current):

            if not current:

                return

            values.append(current.value)
            walk(current.left)
            walk(current.right)

        walk(self.root)

        return values

    def in_order(self):

        values = []

        def walk(current):

            if not current:
                return

            walk(current.left)
            values.append(current.value)
            walk(current.right)

        walk(self.root)

        return values


    def post_order(self):

        values = []

        def walk(current):

            if not current:
                return

            walk(current.left)
            walk(current.right)
            values.append(current.value)

        walk(self.root)

        return values

    def breadth_first(self):

        temp_queue = Queue()
        results = []

        if not self.root:
            return "No bueno"

        temp_queue.enqueue(self.root)

        while temp_queue.peek():
            current_node = temp_queue.dequeue()
            results.append(current_node.value.value)

            if current_node.value.left:
                temp_queue.enqueue(current_node.value.left)

            if current_node.value.right:
                temp_queue.enqueue(current_node.value.right)

        return results



def value_tree(tree1, tree2):

    output = set()
    values1 = tree1.breadth_first()
    values2 = tree2.breadth_first()


    for i in range(len(values1)):
        try:
            if values1[i] == values2[i]:
                output.add(values1[i])
        except IndexError:
            pass
    return output


if __name__ == "__main__":
    tree1 = BinaryTree()
    tree2 = BinaryTree()
    tree1.root = Node(1)
    tree1.root.left = Node(2)
    tree1.root.right = Node(3)
    tree1.root.left.left = Node(4)
    tree1.root.left.right = Node(5)
    tree2.root = Node(1)
    tree2.root.right = Node(3)
    print(tree1.breadth_first())
    print(tree1.pre_order())
