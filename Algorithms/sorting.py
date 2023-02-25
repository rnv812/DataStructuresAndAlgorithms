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


def merge_sort(lst: list) -> None:
    def merge(lst: list, start: int, middle: int, end: int) -> None:
        lst_temp = []
        pos_left = start
        pos_righ = middle

        while pos_left < middle and pos_righ < end:
            if lst[pos_left] < lst[pos_righ]:
                lst_temp.append(lst[pos_left])
                pos_left += 1
            else:
                lst_temp.append(lst[pos_righ])
                pos_righ += 1

        while pos_left < middle:
            lst_temp.append(lst[pos_left])
            pos_left += 1

        while pos_righ < end:
            lst_temp.append(lst[pos_righ])
            pos_righ += 1

        for i, num in enumerate(lst_temp):
            lst[start + i] = num

    def sort(lst: list, start: int, end: int) -> None:
        if (end - start) > 1:
            middle = (end + start) // 2
            sort(lst, start, middle)
            sort(lst, middle, end)
            merge(lst, start, middle, end)

    sort(lst, 0, len(lst))


def quick_sort(lst: list) -> None:
    def partition(lst: list, start: int, end: int) -> int:
        # choose pivot using Lomuto median
        mid = (start + end) // 2
        if lst[mid] < lst[start]:
            lst[mid], lst[start] = lst[start], lst[mid]
        if lst[end - 1] < lst[start]:
            lst[end - 1], lst[start] = lst[start], lst[end - 1]
        if lst[end - 1] < lst[mid]:
            lst[end - 1], lst[mid] = lst[mid], lst[end - 1]
        pivot = lst[mid]

        i = start
        j = end - 1
        while True:
            while lst[i] < pivot:
                i += 1
            while lst[j] > pivot:
                j -= 1
            if i >= j:
                break
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1

        return i

    def sort(lst: list, start: int, end: int) -> None:
        if (end - start) > 1:
            pivot = partition(lst, start, end)
            sort(lst, start, pivot)
            sort(lst, pivot, end)

    sort(lst, 0, len(lst))
