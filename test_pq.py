import random

from adt.stack_queue.pq import PriorityQueue


if __name__ == "__main__":
    pq = PriorityQueue()

    print("is_empty:", pq.is_empty())

    for i in range(1, 10):
        index = random.randint(1, 5)
        print(f"enqueue p{index} d{i}: {pq.enqueue(index, i)}")
        print(f"len: {len(pq)}")
        print(f"front: {pq.front()}")

    print(pq)
    print("is_empty:", pq.is_empty())

    while not pq.is_empty():
        print(f"dequeue: [is_empty: {pq.is_empty()}, front: {pq.front()}]")
        print(pq.dequeue())

    print(f"dequeue: [is_empty: {pq.is_empty()}, front: {pq.front()}]")
    print(pq.dequeue())
