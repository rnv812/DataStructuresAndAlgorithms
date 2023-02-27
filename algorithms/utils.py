from random import randint
from typing import List


def get_random_list(size: int = 10, min_: int = -10, max_: int = 10) -> List[int]:
    return [randint(min_, max_) for _ in range(size)]
