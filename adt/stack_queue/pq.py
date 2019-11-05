from adt.stack_queue.queue import Queue
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
        self.__front = None, 0

    def is_empty(self) -> bool:
        return self.__front == (None, 0)

    def enqueue(self, priority: int, data: object) -> bool:
        """
        Método que adiciona un nuevo Nodo con su dato
        correspondiente, según la prioridad que éste tendrá.
        priority → [1 > 2 > 3 > ... > n]
        """
        if self.is_empty():
            new_queue = Queue()
            new_queue.enqueue(data)
            new_node = QueueNode(new_queue)
            self.front = new_node, priority
        elif type(data) == type(self.front()):
            current_node = self.front
            while current_node[0]:
                if current_node[1] == priority:
                    current_node[0].data.enqueue(data)
                    break
                else:
                    current_node = current_node[0].next
            new_queue = Queue()
            new_queue.enqueue(data)
            new_node = QueueNode(new_queue)
            current_node[0].next = new_node, priority
        else:
            return False
        return True

    def dequeue(self) -> object:
        data = self.__front[0].data.dequeue()
        if self.__front[0].is_empty():
            self.__front = self.__front[0].next, self.__front[0].next[1]
        return data

    def front(self) -> object:
        return self.__front[0].data.front()

    def __len__(self) -> int:
        cnt = 0
        current_node = self.__front[0]
        while current_node:
            cnt += len(current_node.data)
            current_node = current_node.next[0]
        return cnt

    def __str__(self) -> str:
        string = ''
        current_node = self.__front[0]
        while current_node:
            string += str(current_node.data) + '\n'
            current_node = current_node.next[0]
        return string
