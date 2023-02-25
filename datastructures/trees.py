from typing import List
from random import randint


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root: Node = None) -> None:
        self.root = root


class BST(Tree):
    def add(self, node: Node):
        def add(tree_node: Node, node: Node):
            if node.value < tree_node.value:
                if tree_node.left is None:
                    tree_node.left = node
                else:
                    add(tree_node.left, node)
            else:
                if tree_node.right is None:
                    tree_node.right = node
                else:
                    add(tree_node.right, node)

        if self.root is None:
            self.root = node
        else:
            add(self.root, node)

    def remove(self, value: int):
        raise NotImplementedError

    def inorder_traversal(self) -> List[int]:
        values = []

        def inorder_traversal(node: Node):
            if node is None:
                return
            inorder_traversal(node.left)
            values.append(node.value)
            inorder_traversal(node.right)

        inorder_traversal(self.root)

        return values


def main():
    tree = BST()
    values = [randint(-10, 10) for i in range(20)]

    for value in values:
        tree.add(Node(value))

    print('Original values:', values)
    print('In order traversal:', tree.inorder_traversal())
