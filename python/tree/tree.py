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



class BinarySearchTree(BinaryTree):

    def __init__(self):
        self.root = None

    def add(self, value):

        def walk(node, value):

            new_node = Node(value)

            if node is None:
                self.root = new_node
                return
                
            if value < node.value:

                if not node.left:
                    node.left = new_node

                else:
                   walk(node.left)

            else:

                if not node.right:
                    node.right = new_node

                else:
                    walk(node.right)

        walk(self.root, value)

    def contains(self, value):


        def walk(node):

            if not node:
                return False

            if node.value == value:

                return True

            else:
                # if value is less than nodes value walk left if value is greater than nodes value walk right
                if value < node.value:
                    return walk(node.left)

                else:
                    return walk(node.right)


        found = walk(self.root)
        return found
