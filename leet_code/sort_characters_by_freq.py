from collections import Counter

def frequencySort(s: str):
    if len(s) <= 1:
        return s
    counts = Counter(s)
    ans = []
    items = [[v, k] for k, v in counts.items()]
    items.sort(reverse=True)
    for k, v in items:
        ans.append(k * v)
    return "".join(ans)

print(frequencySort('aab'))