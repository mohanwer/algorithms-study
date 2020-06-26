def most_common(words: [str]):
    from collections import Counter
    word_dict = Counter(words)
    most_common = []
    for k, v in word_dict.items():
        if len(most_common) == 0:
            most_common.append((k, v))
        else:
            if most_common[0][1] == v:
                most_common.append((k, v))
            elif most_common[0][1] < v:
                most_common = [(k, v)]
    return [w[0] for w in most_common]


w = ["a"]
z = most_common(w)