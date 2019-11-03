# from adt.lists.sll import SinglyLinkedList
# from adt.stack_queue.queue import Queue
# from adt.stack_queue.stack import Stack

from adt.stack_queue.nodes import QueueNode

class PriorityQueue:
    """
    Clase que implementa el funcionamiento del ADT Priority
    Queue, utilizando varias Queues, según el número de
    prioridades existentes. Serán atendidos, o tienen MAYOR
    prioridad, los Nodos que se encuentren en las Queues que
    manejen un valor de prioridad menor.
    """

    def __init__(self) -> None:
        self.front = None
        self.tail = None

    def is_empty(self) -> bool:
        return self.__front == None

    def enqueue(self, priority: int, data: object) -> bool:
        """
        Método que adiciona un nuevo Nodo con su dato
        correspondiente, según la prioridad que éste tendrá.
        priority → [1 > 2 > 3 > ... > n]
        """
        pass

    def dequeue(self) -> object:
        pass

    def front(self) -> object:
        pass

    def __len__(self) -> int:
        pass

    def __str__(self) -> str:
        pass
