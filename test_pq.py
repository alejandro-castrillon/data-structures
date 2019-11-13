import random

from adt.stack_queue.pq import PriorityQueueNodes as PriorityQueue


if __name__ == "__main__":
    pq = PriorityQueue()

    print("is_empty:", pq.is_empty())
    print(f"dequeue: [is_empty: {pq.is_empty()}, front: {pq.front()}]")
    print(pq.dequeue())
    print(pq)

    print(f"enqueue d{4} p{'3'} ")
    print(f"len: {len(pq)}")
    print(f"front: {pq.front()}")
    print("enqueued", pq.enqueue(4, "3"))
    print(pq)

    for i in range(1, 10):
        index = random.randint(1, 5)
        print(f"enqueue d{i} p{index} ")
        print(f"len: {len(pq)}")
        print(f"front: {pq.front()}")
        print("enqueued", pq.enqueue(i, index))
        print(pq)

    print("is_empty:", pq.is_empty())

    cnt = 0
    while not pq.is_empty() and cnt <= len(pq) / 2:
        print(f"dequeue: [is_empty: {pq.is_empty()}, front: {pq.front()}]")
        print(pq.dequeue())
        print(pq)
        cnt += 1

    print(f"enqueue d{4} p{'3'} ")
    print(f"len: {len(pq)}")
    print(f"front: {pq.front()}")
    print("enqueued", pq.enqueue(4, "3"))
    print(pq)

    for i in range(10, 20):
        index = random.randint(1, 6)
        print(f"enqueue d{i} p{index} ")
        print(f"len: {len(pq)}")
        print(f"front: {pq.front()}")
        print("enqueued", pq.enqueue(i, index))
        print(pq)

    while not pq.is_empty():
        print(f"dequeue: [is_empty: {pq.is_empty()}, front: {pq.front()}]")
        print(pq.dequeue())
        print(pq)

    print(f"dequeue: [is_empty: {pq.is_empty()}, front: {pq.front()}]")
    print(pq.dequeue())
