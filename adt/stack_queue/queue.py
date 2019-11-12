from adt.stack_queue.nodes import QueueNode


class Queue:
    def __init__(self) -> None:
        self._front = self.tail = None

    def is_empty(self) -> bool:
        return self._front == self.tail == None

    def enqueue(self, data) -> bool:
        new_node = QueueNode(data)
        if self.is_empty():
            self._front = self.tail = new_node
        elif type(data) == type(self.front()):
            self.tail.next = self.tail = new_node
        else:
            return False
        return True

    def dequeue(self) -> object:
        if not self.is_empty():
            data, self._front = self.front(), self._front.next
            if not self._front:
                self.tail = self._front
            return data

    def front(self) -> object:
        if not self.is_empty():
            return self._front.data

    def __str__(self) -> str:
        current_node = self._front
        acm = ""
        while current_node:
            acm += str(current_node.data) + "\n"
            current_node = current_node.next
        return acm

    def __len__(self) -> int:
        cnt = 0
        current_node = self._front
        while current_node:
            cnt += 1
            current_node = current_node.next
        return cnt
