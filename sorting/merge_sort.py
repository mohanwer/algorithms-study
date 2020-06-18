# https://en.wikipedia.org/wiki/Merge_sort

def merge_sort(collection):
    def merge(left, right):
        result = []
        while left and right:
            result.append((left if left[0] <= right[0] else right).pop(0))
        return result + left + right

    if len(collection) <= 1:
        return collection
    mid = len(collection) // 2
    return merge(merge_sort(collection[mid:]), merge_sort(collection[:mid]))

result = merge_sort([0, 5, 3, 2, 2])