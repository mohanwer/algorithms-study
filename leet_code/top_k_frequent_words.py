# https://leetcode.com/problems/top-k-frequent-words/

from typing import List

class Word:

    def __init__(self, freq, word):
        self.freq = freq
        self.word = word

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq

    def __eq__(self, other):
        return self.freq == self.freq and self.word == self.word


def topKFrequent2(words: List[str], k: int) -> List[str]:
    from collections import Counter
    import heapq
    word_dict = Counter(words)
    res = []
    for key, value in word_dict.items():
        heapq.heappush(res, Word(value, key))
    answer = [heapq.heappop(res).word for _ in range(k)]
    return answer[::-1]


def topKFrequent(words: List[str], k: int) -> List[str]:
    from collections import Counter
    word_dict = Counter(words)
    word_list = [(word_dict[word], word) for word in word_dict.keys()]
    word_list = sorted(word_list, key=lambda x: (-x[0], x[1]))
    return word_list[:k]


question = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
z = topKFrequent2(question, 4)