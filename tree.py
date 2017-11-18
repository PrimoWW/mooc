class Node():
    def __init__(self, item):
        self.item = item
        self.left_child = None
        self.right_child = None


class Tree():
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)

        if self.root is None:
            self.root = node
        else:
            q = [self.root]

            while True:
                pop_node = q.pop(0)

                if pop_node.left_child is None:
                    pop_node.left_child = node
                    return
                elif pop_node.right_child is None:
                    pop_node.right_child = node
                    return
                else:
                    q.append(pop_node.left_child)
                    q.append(pop_node.right_child)

    def pre_order(self, root):
        if root is None:
            return []
        result = [root.item]
        left_item = self.pre_order(root.left_child)
        right_item = self.pre_order(root.right_child)
        return result + left_item + right_item

    def exchange(self, root):
        if root is None:
            return []
        if root.left_child is None and root.right_child is None:
            return
        else:
            root.left_child, root.right_child = root.right_child, root.left_child
            self.exchange(root.left_child)
            self.exchange(root.right_child)

t = Tree()
t.add('A')
t.add('B')
t.add('C')
t.add('D')
t.add('E')
t.add('F')
t.add('G')
print(t.pre_order(t.root))
t.exchange(t.root)
print(t.pre_order(t.root ))