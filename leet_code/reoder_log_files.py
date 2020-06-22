# https://leetcode.com/problems/reorder-data-in-log-files/submissions/

from typing import List

class Log:
    def __init__(self, log: str):
        split_log = log.split(" ")
        self.log: str = log
        self.numeric = split_log[1].isnumeric()
        self.log_order = log.split(" ")[1:]

    def __lt__(self, other):
        if not self.numeric and not other.numeric:
            if self.log_order == other.log_order:
                return self.log < other.log
            return self.log_order < other.log_order
        elif other.numeric and not self.numeric:
            return True
        else:
            return False


def reorderLogFiles(logs: List[str]) -> List[str]:
    answer: [Log] = []
    for log in logs:
        answer.append(Log(log))
    return [a.log for a in sorted(answer)]

v = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]
z = reorderLogFiles(v)