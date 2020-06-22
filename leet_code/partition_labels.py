# https://leetcode.com/problems/partition-labels/

from typing import List
from collections import defaultdict

def partitionLabels(S: str) -> List[int]:
    letters = defaultdict(list)
    for i, k in enumerate(S):
        if k not in letters:
            letters[k] = [i, i]
        else:
            letters[k][1] = i

    answer = []
    lap = letters[S[0]][1]
    for letter in letters:
        next_start = letters[letter][0]
        next_end = letters[letter][1]
        if lap > next_start and lap < next_end:
            lap = next_end
        elif lap < next_start:
            if len(answer) == 0:
                answer.append(next_start)
            else:
                answer.append(next_start - sum(answer))
            lap = next_end
    closing = len(S) - sum(answer)
    answer.append(closing)
    return letters, answer

a = "dccccbaabe"
c, z = partitionLabels(a)