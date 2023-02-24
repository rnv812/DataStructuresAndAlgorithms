from random import randint
from sorting import *
from typing import List, Callable


def get_random_list(size: int, min: int, max: int) -> List[int]:
    return [randint(min, max) for _ in range(size)]


def try_random_cases(sorting_function: Callable, num_cases: int = 10):
    for _ in range(num_cases):
        input_list = get_random_list(10, -10, 10)
        expected_list = sorted(input_list)

        sorting_function(input_list)

        assert input_list == expected_list


def test_bubble_sort():
    try_random_cases(bubble_sort)


def test_selection_sort():
    try_random_cases(selection_sort)


def test_insertion_sort():
    try_random_cases(insertion_sort)


def test_merge_sort():
    try_random_cases(merge_sort)