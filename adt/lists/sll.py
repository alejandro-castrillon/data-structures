from adt.lists.nodes import SinglyLinkedNode


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node.data
            current_node = current_node.next

    def __str__(self):
        string = ""
        for i in self:
            string += str(i)+ '\n'
        return string

    def __len__(self):
        cnt = 0
        for _ in self:
            cnt += 1
        return cnt

    def is_empty(self):
        return self.head == None

    def append(self, new_data):
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

    def insert(self, new_data, pos=0):
        new_node = SinglyLinkedNode(new_data)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
        elif pos == len(self):
            return self.append(new_data)
        elif pos < len(self):
            cnt = 0
            current_node = self.head
            while cnt < pos - 1:
                current_node = current_node.next
            current_node.next, new_node.next = new_node, current_node.next
        else:
            return False
        return True

    def delete(self, data, all=False):
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

    def remove(self, pos):
        if not self.is_empty():
            return self.delete(self.locate(pos))

    def search(self, data):
        for i in self:
            if i == data:
                return i

    def locate(self, pos):
        cnt = 0
        for i in self:
            if cnt == pos:
                return i
            cnt += 1
            
    def explorer(self):
        print(self)

    # def reverse(self):
    #     pass
    


# def bubblesort(_list):
#     for i in range(len(_list)-1,0,-1):
#         for j in range(i):
#             if _list[j]>_list[j+1]:
#                 _list[j],_list[j+1]=_list[j+1],_list[j]
#                 # aux =_list[j]
#                 # _list[j]=_list[j+1]
#                 # _list[j+1] =aux
