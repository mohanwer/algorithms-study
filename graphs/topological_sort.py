#https://leetcode.com/problems/course-schedule/
from typing import List
import collections

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for req, nezt in prerequisites:
            adj[nezt].append(req)
            indegree[req] += 1

        q = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        visited = 0
        while q:
            node = q.popleft()
            visited += 1

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return visited == numCourses

assert canFinish(2, [[1,0]])