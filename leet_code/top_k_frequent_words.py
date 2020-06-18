# https://leetcode.com/problems/top-k-frequent-words/
from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_dict = defaultdict()

        for word in words:
            if not word_dict[word]:
                word