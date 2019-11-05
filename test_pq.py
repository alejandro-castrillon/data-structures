from adt.stack_queue.pq import PriorityQueue

if __name__ == "__main__":
	pq = PriorityQueue()
	
	print('is_empty:', pq.is_empty())

	print('enqueue 1 1:', pq.enqueue('1', 1))
	
	print('is_empty:', pq.is_empty())

	print('enqueue 2 2:', pq.enqueue('2', 2))
	print('enqueue 3 3:', pq.enqueue('3', 3))
	print('enqueue 4 2:', pq.enqueue('4', 2))

	print('enqueue 5 1:', pq.enqueue('5', 1))
	print('enqueue 6 3:', pq.enqueue('6', 3))

	print('enqueue 7 1:', pq.enqueue('7', 1))
	print('enqueue 8 4:', pq.enqueue('8', 4))
	print('enqueue 9 3:', pq.enqueue('9', 3))

	print(pq)
