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

    def find_maximum_value(self):

        current = self.root

        if not self.root:
            return "I pitty the empty fool!"

        def walk(root):
            nonlocal current

            if not root:
                return
            if root.value > current.value:
                current = root

            walk(root.left)
            walk(root.right)

        walk(self.root)

        return current.value

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


def tree_intersections():
    
