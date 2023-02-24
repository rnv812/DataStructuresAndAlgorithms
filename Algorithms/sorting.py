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
    for step in range(n):
        min_idx = step
        for i in range(step + 1, n):
            if lst[i] < lst[min_idx]:
                min_idx = i
        lst[step], lst[min_idx] = lst[min_idx], lst[step]
