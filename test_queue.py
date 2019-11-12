from adt.stack_queue.queue import Queue

if __name__ == '__main__':
    queue = Queue()

    print('is_empty:', queue.is_empty())
    print('len:', len(queue))
    print('front:', queue.front())

    print('dequeue:', queue.dequeue())

    print('enqueue 3:', queue.enqueue(3))

    print('is_empty:', queue.is_empty())
    print('queue:', queue)
    print('front:', queue.front())
    print('len:', len(queue))

    print('enqueue "5":', queue.enqueue('5'))

    print('dequeue:', queue.dequeue())

    print('enqueue 9:', queue.enqueue(9))
    print('queue:', queue)
    print('front:', queue.front())
    print('len:', len(queue))

    for i in range(8, -1, -1):
        print(f'enqueue {i}:', queue.enqueue(i))
    print('queue:', queue)
    print('front:', queue.front())
    print('len:', len(queue))

    for i in range(len(queue) + 1):
        print('-------------')
        print('queue:', queue, sep='\n')
        print('front:', queue.front())
        print('len:', len(queue))
        print('dequeue:', queue.dequeue())
