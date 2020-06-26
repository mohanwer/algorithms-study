# https://leetcode.com/problems/search-suggestions-system/

from typing import List

def suggestedProducts(products: List[str], searchWord: str) -> List[List[str]]:
    products.sort()

    def search(words, item):
        left = 0
        right = len(words) - 1
        answer = []
        while left <= right:
            midpoint = left + (right - left)
            current = words[midpoint]
            if current.startswith(item):
                return window(words, midpoint, item)
            elif current > item:
                right = midpoint - 1
            else:
                left = midpoint + 1
        return answer

    def window(words, position, item):
        end = start = position
        while start-1 >= 0 and words[start-1].startswith(item):
            start -= 1
        diff = position - start
        if diff >= 3:
            return words[start:start+3]

        while end-start+1<=3 and end+1<=len(words)-1 and words[end+1].startswith(item):
            end += 1
        return words[start:end+1]

    answer = []
    for i in range(len(searchWord)):
        word = searchWord[:i+1]
        result = search(products, word)
        answer.append(result)

    return answer

products = ["mobile","mouse","moneypot","monitor","mousepad"]
z = suggestedProducts(products, "mouse")