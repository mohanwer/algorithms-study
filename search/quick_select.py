import random


def _partition(data: list, pivot) -> tuple:
    small, equal, big = [], [], []
    for element in data:
        if pivot > element:
            small.append(element)
        elif pivot < element:
            big.append(element)
        else:
            equal.append(element)
    return (small, equal, big)


def quick_select(items: list, index: int):
    if index > len(items) or index < 0:
        return None

    pivot = random.randint(0, len(items) - 1)
    pivot = items[pivot]
    small, equal, big = _partition(items, pivot)
    small_count = len(small)
    equal_count = len(equal)

    if small_count <= equal_count < small_count + equal_count:
        return pivot
    if small_count > index:
        return quick_select(small, index)
    else:
        return quick_select(big, index - (small_count + equal_count))


result = quick_select([2, 4, 5, 7, 899, 54, 32], 5)
