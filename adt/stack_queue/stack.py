from adt.stack_queue.nodes import StackNode


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = StackNode(data)
        if self.is_empty():
            self.top = new_node
        elif type(data) == type(self.top.data):
            new_node.next = self.top
            self.top = new_node
        else:
            return False
        return True

    def pop(self):
        if not self.is_empty():
            data_ret = self.top.data
            self.top = self.top.next
            return data_ret

    def peek(self):
        if not self.is_empty():
            return self.top.data

    def __str__(self):
        current_node = self.top
        string = ""
        while current_node is not None:
            string += str(current_node.data) + "\n"
            current_node = current_node.next
        return string

    def __len__(self):
        cnt = 0
        current_node = self.top
        while current_node is not None:
            cnt += 1
            current_node = current_node.next
        return cnt
