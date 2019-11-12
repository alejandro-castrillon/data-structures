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

    def enqueue(self, priority: int, data: object) -> bool:
        """
        Método que adiciona un nuevo Nodo con su dato
        correspondiente, según la prioridad que éste tendrá.
        priority → [1 > 2 > 3 > ... > n]
        """
        if priority >= 1:
            if self.is_empty():
                new_queue = Queue()
                new_queue.enqueue(data)
                if type(priority) == int:
                    return self.priorities.append(
                        priority
                    ) and self.queues.append(new_queue)
            elif type(data) == type(self.front()):
                return self.__enqueue(priority, data)
        return False

    def __enqueue(self, priority: int, data: object) -> bool:
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
                    return self.priorities.insert(
                        priority, i
                    ) and self.queues.insert(new_queue, i)

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

    def enqueue(self, priority: int, data: object) -> bool:
        """
        Método que adiciona un nuevo Nodo con su dato
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
                    return self.enqueue(priority, data)

        return False

    def dequeue(self) -> object:
        for i in self.queues:
            if not i.is_empty():
                return i.dequeue()

    def front(self) -> object:
        for i in self.queues:
            if not i.is_empty():
                return i.front

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
    def enqueue(self, new_data: object, priority: int = 1) -> bool:
        if priority >= 1:
            new_node = PriorityNode(new_data, priority)
            if self.is_empty():
                self._front = self.tail = new_node
                print(
                    'empty enqueued, data:',
                    new_node.data,
                    'priority:',
                    new_node.priority,
                    'front data:',
                    self._front.data,
                    'front priority:',
                    self._front.priority,
                )
                return True
            elif type(new_data) == type(self.front()):
                self.__enqueue(new_data, priority)
                return True
        return False

    def __enqueue(self, new_data, priority):
        new_node = PriorityNode(new_data, priority)

        finded = False
        current_node = self._front
        while current_node:
            if current_node.priority == priority:
                finded = True
                break
            current_node = current_node.next

        if finded:
            current_node = self._front
            while current_node:
                if priority > current_node.priority:
                    current_node.next, new_node.next = (
                        new_node,
                        current_node.next,
                    )
                    break
                current_node = current_node.next
        else:
            self.tail.next = self.tail = new_node
