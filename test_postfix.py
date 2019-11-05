from adt.stack_queue.notation import Postfix

if __name__ == "__main__":
    # postfix = Postfix("   31^20      + 50(6    -98765432 1)/     -21    .   245    ")
    postfix = Postfix("12 * 3 - 9 + 4.5 * 6.78")
    print(postfix.infix())
    print(postfix.postfix())
    