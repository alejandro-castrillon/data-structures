from adt.stack_queue.nodes import QueueNode

class Queue:
    def __init__(self):
        self.front = None
        self.tail = None

    def is_empty(self):
        return self.front == None

    def enqueue(self, data):
        new_node = QueueNode(data)
        if self.is_empty():
            self.front = new_node
            self.tail = new_node
        elif type(data) == type(self.tail.data):
            self.tail.next = new_node
            self.tail = new_node
        else:
            return False
        return True

    def dequeue(self):
        if not self.is_empty():
            data_ret = self.front.data
            self.front = self.front.next
            return data_ret

    def front(self, data):
        if not self.is_empty():
            return self.front.data

    def __str__(self):
        current_node = self.front
        string = ""
        while current_node:
            string += str(current_node.data) + "\n"
            current_node = current_node.next
        return string

    def __len__(self):
        cnt = 0
        current_node = self.front
        while current_node:
            cnt += 1
            current_node = current_node.next
        return cnt
