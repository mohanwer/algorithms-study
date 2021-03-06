import random

def quickselect(items, index):

    def select(lst, l, r, index):
        if r == l:
            return lst[l]

        pv = random.randint(l, r)
        lst[pv], lst[l] = lst[l], lst[pv]
        i = l
        for j in range(l + 1, r + 1):
            if lst[j] > lst[l]:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]

        lst[l], lst[i] = lst[i], lst[l]
        if index == i:
            return lst[i]
        elif index < i:
            return select(lst, l, i -1, index)
        else:
            return select(lst, i + 1, r, index)

    if items is None or len(items) < 1:
        return None
    return select(items, 0, len(items) - 1, index)

result = quickselect([2, 4, 5, 7, 899, 54, 32], 0)
