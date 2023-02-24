def bubble_sort(lst: list) -> None:
    n = len(lst)
    swapped = False
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break


def selection_sort(lst: list) -> None:
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]


def insertion_sort(lst: list) -> None:
    n = len(lst)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if lst[j] < lst[i]:
                lst[i], lst[j] = lst[j], lst[i]
