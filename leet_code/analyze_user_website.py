from typing import List
from collections import defaultdict
from itertools import combinations


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        all_data = [(t, u, w) for u, t, w in zip(username, timestamp, website)]
        all_data.sort()

        users_visits = defaultdict(list)
        for t, u, w in all_data:
            users_visits[u].append(w)

        counter_dict = defaultdict(int)
        for website_list in users_visits.values():
            combs = set(combinations(website_list, 3))
            for comb in combs:
                counter_dict[comb] += 1

        sorted_dict = sorted(counter_dict, key=lambda x: (-counter_dict[x], x))
        return sorted_dict[0]

usernames =  ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamps = [1,2,3,4,5,6,7,8,9,10]
websites = ["home","about","career","home","cart","maps","home","home","about","career"]

g = Solution()
print(g.mostVisitedPattern(usernames, timestamps, websites))