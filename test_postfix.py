from adt.stack_queue.notation import Postfix

if __name__ == "__main__":
    postfix = Postfix("(6+4)*8*(7+4)")
    print(postfix.infix())
    print(postfix.postfix())
    print(postfix.arithmetic_expression_evaluation())

    print("-" * 10)
    postfix = Postfix("(6+2)*3/2^2-4")
    print(postfix.infix())
    print(postfix.postfix())
    print(postfix.arithmetic_expression_evaluation())

    print("-" * 10)
    postfix = Postfix("0.5 * 15 + 2 * 10")
    print(postfix.infix())
    print(postfix.postfix())
    print(postfix.arithmetic_expression_evaluation())

    print("-" * 10)
    postfix = Postfix("( 12 + 7.5 ) * 3 - ( 0.1203 - 0.003 ) * ( 5 + 25 )")
    print(postfix.infix())
    print(postfix.postfix())
    print(postfix.arithmetic_expression_evaluation())

    print("-" * 10)
    postfix = Postfix("3 + 4 - 5 ")
    print(postfix.infix())
    print(postfix.postfix())
    print(postfix.arithmetic_expression_evaluation())

    print("-" * 10)
    postfix = Postfix("3 + 2 *4 ")
    print(postfix.infix())
    print(postfix.postfix())
    print(postfix.arithmetic_expression_evaluation())

    print("-" * 10)
    postfix = Postfix("(3 + 2) *4 ")
    print(postfix.infix())
    print(postfix.postfix())
    print(postfix.arithmetic_expression_evaluation())

    print("-" * 10)
    postfix = Postfix("3 + 4 * (5 - 2)")
    print(postfix.infix())
    print(postfix.postfix())
    print(postfix.arithmetic_expression_evaluation())

    print("-" * 10)
    postfix = Postfix("7 * 3 - 6 / 2 + 4 ^ 2")
    print(postfix.infix())
    print(postfix.postfix())
    print(postfix.arithmetic_expression_evaluation())

    print("-" * 10)
    postfix = Postfix("(3^2 - 2 * 3 + 8 / 2)^2")
    print(postfix.infix())
    print(postfix.postfix())
    print(postfix.arithmetic_expression_evaluation())

    print("-" * 10)
    postfix = Postfix("4 ^ 3 ^ 2 ^ 1")
    print(postfix.infix())
    print(postfix.postfix())
    print(postfix.arithmetic_expression_evaluation())
