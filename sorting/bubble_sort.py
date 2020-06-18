# https://github.com/TheAlgorithms/Python/blob/master/sorts/bubble_sort.py


def bubble_sort(collection):
    length = len(collection) - 1
    for i in range(length):
        swapped = False
        for j in range(length - i):
            if collection[j+1] < collection[j]:
                swapped = True
                collection[j+1], collection[j] = collection[j], collection[j+1]
        if not swapped:
            break
    return collection


result = bubble_sort([-23, 0, 6, -4, 34])