"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool

>>> find_occurrences(example_tree, "RED")
6
>>> find_occurrences(example_tree, "of")
2
>>> find_occurrences(example_tree, "BLUE")
2
>>> find_occurrences(example_tree, "jopa")
0
"""
from typing import Any

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
    },
    "fourth": "RED",
}


def find_occurrences(tree: dict, element: Any) -> int:
    if element == tree:
        return 1
    elif isinstance(tree, (list, tuple, set)):
        return sum(find_occurrences(node, element) for node in tree)
    elif isinstance(tree, dict):
        return sum(find_occurrences(value, element) for value in tree.values())
    return 0


if __name__ == '__main__':
    print(find_occurrences(example_tree, "RED"))  # 6
