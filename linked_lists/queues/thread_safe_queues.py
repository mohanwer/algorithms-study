from multiprocessing import Process, Lock, Queue, Pool
import threading

q = Queue()
size = 10
for i in range(size):
    q.put(i)


def remove_last_record(mp_queue: Queue) -> None:
    rec = mp_queue.get()
    print(rec)


p1 = Process(target=remove_last_record, args=(q,))
p2 = Process(target=remove_last_record, args=(q,))
p1.start()
p2.start()
p1.join()
p2.join()
