from datastructures import trees
from utils import get_random_list


def test_bst_inorder_traversal():
    tree = trees.BST()
    values = get_random_list()
    for value in values:
        tree.add(trees.Node(value))

    assert sorted(values) == tree.inorder_traversal()
