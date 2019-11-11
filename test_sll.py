from adt.lists.sll import SinglyLinkedList

if __name__ == "__main__":
    sll = SinglyLinkedList()

    print("is empty:", sll.is_empty())

    print("remove 0:", sll.remove(0))
    print("remove 1:", sll.remove(1))

    print("insert 0 1:", sll.insert(0, 1))
    print(sll)

    print("is empty:", sll.is_empty())

    print("insert 0 1:", sll.insert(0, -1))
    print(sll)

    print("insert 0 1:", sll.insert(0, 0))
    print(sll)

    print("is empty:", sll.is_empty())

    for i in range(1, 10):
        sll.append(i)
    print(sll)
