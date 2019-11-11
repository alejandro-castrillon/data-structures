from adt.stack_queue.nodes import QueueNode


class Queue:
    def __init__(self) -> None:
        self.__front = self.tail = None

    def is_empty(self) -> bool:
        return self.__front == None

    def enqueue(self, data) -> bool:
        new_node = QueueNode(data)
        if self.is_empty():
            self.__front = new_node
            self.tail = self.__front
        elif type(data) == type(self.tail.data):
            self.tail.next = new_node
            self.tail = new_node
        else:
            return False
        return True

    def dequeue(self) -> object:
        if not self.is_empty():
            data = self.front
            self.__front = self.__front.next
            return data

    @property
    def front(self) -> object:
        if not self.is_empty():
            return self.__front.data

    def __str__(self) -> str:
        current_node = self.__front
        acm = ""
        while current_node:
            acm += str(current_node.data) + "\n"
            current_node = current_node.next
        return acm

    def __len__(self) -> int:
        cnt = 0
        current_node = self.__front
        while current_node:
            cnt += 1
            current_node = current_node.next
        return cnt
