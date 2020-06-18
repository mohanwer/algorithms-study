# https://en.wikipedia.org/wiki/Insertion_sort


def insertion_sort(collection):
    for i in range(1, len(collection)):
        while i > 0 and collection[i - 1] > collection[i]:
            collection[i - 1], collection[i] = collection[i], collection[i - 1]
            i -= 1
    return collection


result = insertion_sort([0, 5, 3, 2, 2])