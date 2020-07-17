import heapq
from typing import List


def minMeetingRooms(intervals: List[List[int]]) -> int:
    if len(intervals) <= 1:
        return 1
    rooms = []
    intervals.sort()
    heapq.heapify(rooms)
    max_rooms = 1
    for i in range(0, len(intervals)):
        start_time, end_time = intervals[i]
        if not rooms:
            heapq.heappush(rooms, [end_time, start_time])
        elif start_time < rooms[0][0]:
            heapq.heappush(rooms, [end_time, start_time])
            max_rooms = max(len(rooms), max_rooms)
        else:
            while rooms and start_time >= rooms[0][0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, [end_time, start_time])

    return max_rooms

print(minMeetingRooms([[26,29],[19,26],[19,28],[4,19],[4,25]]))