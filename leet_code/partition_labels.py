# https://leetcode.com/problems/partition-labels/

from typing import List
from collections import defaultdict

def partitionLabels(S) -> List[int]:
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

a = ["a", "b", "c", "d", "a", "e", "f", "g", "h", "i", "j", "e"]
c, z = partitionLabels(a)


def lengthEachScene(inputList):
    if len(inputList) == 0:
        return []

    letters = {}

    for i, v in enumerate(inputList):
        if v not in letters:
            letters[v] = [i, i]
        else:
            letters[v][1] = i

    answer = []
    overlap = letters[inputList[0]][1]

    for letter in letters:
        scene_start = letters[letter][0]
        scene_end = letters[letter][1]
        if overlap > scene_start and overlap < scene_end:
            overlap = scene_end
        elif overlap < scene_start:
            if len(answer) == 0:
                answer.append(scene_start)
            else:
                answer.append(scene_start - sum(answer))
            overlap = scene_end

    closing_scene = len(inputList) - sum(answer)
    answer.append(closing_scene)

    return answer


a = ['z']
v = lengthEachScene(a)

from collections import defaultdict


def lengthEachScene(inputList):
    if inputList is None or len(inputList) == 0:
        return []

    letters = {}

    for i, v in enumerate(inputList):
        if v not in letters:
            letters[v] = [i, i]
        else:
            letters[v][1] = i

    s = []
    overlap = letters[inputList[0]][1]
    for letter in letters:
        scene_start = letters[letter][0]
        scene_end = letters[letter][1]
        if overlap > scene_start and overlap < scene_end:
            overlap = scene_end
        elif overlap < scene_start:
            if len(s) == 0:
                s.append(scene_start)
            else:
                s.append(scene_start - sum(s))
            overlap = scene_end

    if len(s) > 0:
        closing_scene = len(inputList) - sum(s)
        s.append(closing_scene)

    return s