class SinglyLinkedNode:
    def __init__(self, data: object) -> None:
        self.data = data
        self.next = None


class DoubleLinkedNode(SinglyLinkedNode):
    def __init__(self, data: object) -> None:
        super().__init__(data)
        self.previous = None
