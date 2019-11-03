from adt.stack_queue.notation import Postfix

if __name__ == "__main__":
    postfix = Postfix("    31^20      + 50(6    -98765432 1)/     -21    .   245    ")
    print(postfix.infix())
    print(postfix.postfix())
