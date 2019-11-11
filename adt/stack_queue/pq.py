from adt.lists.sll import SinglyLinkedList
from adt.stack_queue.queue import Queue


class PriorityQueue:
    """
    Clase que implementa el funcionamiento del ADT Priority
    Queue, utilizando varias Queues, según el número de
    prioridades existentes. Serán atendidos, o tienen MAYOR
    prioridad, los Nodos que se encuentren en las Queues que
    manejen un valor de prioridad menor.
    """

    # Los datos pueden tener prioridad cero o negativa?
    # Los datos deben ser del mismo tipo?

    def __init__(self) -> None:
        self.priorities = SinglyLinkedList()
        self.queues = SinglyLinkedList()

    def is_empty(self) -> bool:
        return self.queues.is_empty() and self.priorities.is_empty()

    def enqueue(self, priority: int, data: object) -> bool:
        """
        Método que adiciona un nuevo Nodo con su dato
        correspondiente, según la prioridad que éste tendrá.
        priority → [1 > 2 > 3 > ... > n]
        """
        enqueued = False

        if self.is_empty():
            new_queue = Queue()
            new_queue.enqueue(data)
            if type(priority) == int:
                enqueued = (
					self.priorities.append(priority)
					and self.queues.append(new_queue)
				)
        elif type(data) == type(self.front()):
            new_queue = Queue()
            new_queue.enqueue(data)
            size = len(self.priorities)

            if self.priorities.search(priority):
                for i in range(len(self.priorities)):
                    if self.priorities.locate(i) == priority:
                        enqueued = self.queues.locate(i).enqueue(data)
                        break
            elif priority < self.priorities.locate(0):
                if self.priorities.insert(priority):
                    enqueued = self.queues.insert(new_queue)
            elif priority > self.priorities.locate(size - 1):
                if self.priorities.insert(priority, size):
                    enqueued = self.queues.insert(new_queue, size)
            else:
                for i in range(len(self.priorities)):
                    if priority < self.priorities.locate(i):
                        enqueued = (
							self.priorities.insert(priority, i)
							and self.queues.insert(new_queue, i)
						)
                        break
        return enqueued

    def dequeue(self) -> object:
        if not self.is_empty():
            data = self.queues.locate(0).dequeue()
            if self.queues.locate(0).is_empty():
                self.queues.remove(0)
                self.priorities.remove(0)
            return data

    def front(self) -> object:
        if not self.is_empty():
            return self.queues.locate(0).front

    def __len__(self) -> int:
        cnt = 0
        for i in self.queues:
            cnt += len(i)
        return cnt

    def __str__(self) -> str:
        acm = ""
        for i in self.queues:
            acm += str(i)
        return acm
