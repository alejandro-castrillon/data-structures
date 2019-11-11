from adt.lists.nodes import SinglyLinkedNode


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def __iter__(self) -> object:
        current_node = self.head
        while current_node:
            yield current_node.data
            current_node = current_node.next

    def __str__(self) -> str:
        acm = ""
        for i in self:
            acm += str(i) + "\n"
        return acm

    def __len__(self) -> int:
        cnt = 0
        for _ in self:
            cnt += 1
        return cnt

    def is_empty(self) -> bool:
        return self.head == None

    def append(self, new_data) -> bool:
        new_node = SinglyLinkedNode(new_data)
        if self.is_empty():
            self.head = new_node
        elif type(new_data) == type(self.head.data):
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
        else:
            return False
        return True

    def insert(self, new_data, pos=0) -> bool:
        new_node = SinglyLinkedNode(new_data)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return True
        elif not self.is_empty() and type(new_data) == type(self.head.data):
            if pos == len(self):
                return self.append(new_data)
            elif 0 < pos < len(self):
                current_node = self.head
                for i in range(pos - 1):
                    current_node = current_node.next
                current_node.next, new_node.next = new_node, current_node.next
                return True
        return False

    def delete(self, data, all=False) -> bool:
        flag = False
        if not self.is_empty():
            if self.head.data == data:
                self.head = self.head.next
                flag = True
            else:
                current_node = self.head
                while current_node.next:
                    if current_node.next.data == data:
                        current_node.next = current_node.next.next
                        flag = True
                        break
                    current_node = current_node.next
        if all and self.search(data):
            flag = self.delete(data)
        return flag

    def remove(self, pos) -> bool:
        if not self.is_empty():
            return self.delete(self.locate(pos))

    def search(self, data) -> object:
        for i in self:
            if i == data:
                return i

    def locate(self, pos) -> object:
        cnt = 0
        for i in self:
            if cnt == pos:
                return i
            cnt += 1

    def explorer(self) -> None:
        print(self)
