def binary_search(sorted_collection, item):
    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        midpoint = left + (right - left)
        current_item = sorted_collection[midpoint]
        if current_item == item:
            return midpoint
        elif current_item > item:
            right = midpoint - 1
        else:
            left = midpoint + 1

    # returns here if not found and returns the left most position
    # where insertion would have happened
    return left


def binary_search_recursion(sorted_collection, item, left, right):
    if left > right:
        return None
    midpoint = left + (right - left)
    curr = sorted_collection[midpoint]
    if curr == item:
        return midpoint
    elif curr > item:
        return binary_search_recursion(sorted_collection, item, left, midpoint - 1)
    else:
        return binary_search_recursion(sorted_collection, item, midpoint + 1, right)