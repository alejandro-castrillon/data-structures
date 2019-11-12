class StackNode:
    def __init__(self, data: object) -> None:
        self.data = data
        self.next = None


class QueueNode:
    def __init__(self, data: object) -> None:
        self.data = data
        self.next = None


class PriorityNode(QueueNode):
    def __init__(self, data: object, priority: int) -> None:
        super().__init__(data)
        self.priority = priority
