from adt.lists.sll import SinglyLinkedList
from adt.stack_queue.queue import Queue
from adt.stack_queue.nodes import PriorityNode


class PriorityQueueLong:
    """
    Clase que implementa el funcionamiento del ADT Priority
    Queue, utilizando varias Queues, según el número de
    prioridades existentes. Serán atendidos, o tienen MAYOR
    prioridad, los Nodos que se encuentren en las Queues que
    manejen un valor de prioridad menor.
    """

    def __init__(self) -> None:
        self.priorities = SinglyLinkedList()
        self.queues = SinglyLinkedList()

    def is_empty(self) -> bool:
        return self.queues.is_empty() and self.priorities.is_empty()

    def enqueue(self, data: object, priority: int) -> bool:
        """
        Método que adiciona un nuevo Nodo con su dato a la Queue
        correspondiente, según la prioridad que éste tendrá.
        priority → [1 > 2 > 3 > ... > n]
        """
        if type(priority) == int and priority > 0:
            if self.is_empty():
                new_queue = Queue()
                new_queue.enqueue(data)
                return self.priorities.append(priority) and self.queues.append(
                    new_queue
                )
            elif type(data) == type(self.front()):
                return self.__enqueue(data, priority)
        return False

    def __enqueue(self, data: object, priority: int) -> bool:
        new_queue = Queue()
        new_queue.enqueue(data)
        size = len(self.priorities)

        if self.priorities.search(priority):
            for i in range(len(self.priorities)):
                if self.priorities.locate(i) == priority:
                    return self.queues.locate(i).enqueue(data)
        elif priority < self.priorities.locate(0):
            if self.priorities.insert(priority):
                return self.queues.insert(new_queue)
        elif priority > self.priorities.locate(size - 1):
            if self.priorities.insert(priority, size):
                return self.queues.insert(new_queue, size)
        else:
            for i in range(len(self.priorities)):
                if priority < self.priorities.locate(i):
                    return self.priorities.insert(priority, i) and self.queues.insert(
                        new_queue, i
                    )

    def dequeue(self) -> object:
        if not self.is_empty():
            data = self.queues.locate(0).dequeue()
            if self.queues.locate(0).is_empty():
                self.queues.remove(0)
                self.priorities.remove(0)
            return data

    def front(self) -> object:
        if not self.is_empty():
            return self.queues.locate(0).front()

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


class PriorityQueueShort:
    """
    Clase que implementa el funcionamiento del ADT Priority
    Queue, utilizando varias Queues, según el número de
    prioridades existentes. Serán atendidos, o tienen MAYOR
    prioridad, los Nodos que se encuentren en las Queues que
    manejen un valor de prioridad menor.
    """

    def __init__(self) -> None:
        self.priorities = SinglyLinkedList()
        self.queues = SinglyLinkedList()

    def is_empty(self) -> bool:
        return len(self) == 0

    def enqueue(self, data: object, priority: int) -> bool:
        """
        Método que adiciona un nuevo Nodo con su dato a la Queue
        correspondiente, según la prioridad que éste tendrá.
        priority → [1 > 2 > 3 > ... > n]
        """
        if type(priority) == int and priority >= 1:
            if self.is_empty() or type(data) == type(self.front()):
                maximum = 0
                for i in self.priorities:
                    maximum = i
                if priority <= maximum:
                    return self.queues.locate(priority - 1).enqueue(data)
                else:
                    self.priorities.append(maximum + 1)
                    self.queues.append(Queue())
                    return self.enqueue(data, priority)
        return False

    def dequeue(self) -> object:
        for i in self.queues:
            if not i.is_empty():
                return i.dequeue()

    def front(self) -> object:
        for i in self.queues:
            if not i.is_empty():
                return i.front()

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


class PriorityQueueNodes(Queue):
    """
    Clase que implementa el funcionamiento del ADT Priority
    Queue, utilizando nodos del tipo PriorityNode. Serán
    atendidos primeramente, o tienen MAYOR prioridad, los
    nodos que por el contrario poseen un valor de prioridad
    menor.
    ATENCIÓN: Esta clase debe soportar el manejo de los
    mismos métodos que implementa una clase Queue, con la
    excepción del método enqueue que posee una
    implementación diferente.
    """

    def enqueue(self, new_data: object, priority: int = 1) -> bool:
        """
        Método que adiciona un nuevo PriorityNode con su dato a la
        PriorityQueue, según la prioridad que éste tendrá. A mayor valor de
        la prioridad el nuevo PriorityNode se ubicará hacia el final de la
        PriorityQueue.
        - Si el nuevo PriorityNode tiene la misma prioridad que uno o varios
        nodos de la PriorityQueue, el nuevo PriorityNode se ubicará
        después del último PriorityNode con la misma prioridad.
        priority → [1 > 2 > 3 > ... > n]
        """
        if type(priority) == int and priority >= 1:
            new_node = PriorityNode(new_data, priority)
            if self.is_empty():
                self._front = self.tail = new_node
                return True
            elif type(new_data) == type(self.front()):
                self.__enqueue(new_data, priority)
                return True
        return False

    def __enqueue(self, new_data: object, priority: int) -> None:
        current_node = self._front
        cnt = 0
        while current_node:
            if priority < current_node.priority:
                break
            else:
                current_node = current_node.next
                cnt += 1

        new_node = PriorityNode(new_data, priority)
        if cnt == 0:
            new_node.next = self._front
            self._front = new_node
        elif 0 < cnt < len(self):
            current_node = self._front
            for i in range(cnt - 1):
                current_node = current_node.next
            current_node.next, new_node.next = new_node, current_node.next
        elif cnt == len(self):
            self.tail.next = new_node
            self.tail = new_node
