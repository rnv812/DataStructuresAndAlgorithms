from algorithms import sorting
from typing import Callable
from utils import get_random_list


def try_random_cases(
        sorting_function: Callable,
        num_cases: int = 10,
):
    for _ in range(num_cases):
        input_list = get_random_list()
        expected_list = sorted(input_list)

        sorting_function(input_list)

        assert input_list == expected_list


def test_bubble_sort():
    try_random_cases(sorting.bubble_sort)


def test_selection_sort():
    try_random_cases(sorting.selection_sort)


def test_insertion_sort():
    try_random_cases(sorting.insertion_sort)


def test_merge_sort():
    try_random_cases(sorting.merge_sort)


def test_quick_sort():
    try_random_cases(sorting.quick_sort)
