from adt.stack_queue.notation import Prefix

if __name__ == "__main__":
    prefix = Prefix("(6+4)*8*(7+4)")
    print(prefix.infix())
    print(prefix.prefix())
    print(prefix.arithmetic_expression_evaluation())
    
    print('-'*10)
    prefix = Prefix("(6+2)*3/2^2-4")
    print(prefix.infix())
    print(prefix.prefix())
    print(prefix.arithmetic_expression_evaluation())
    
    print('-'*10)
    prefix = Prefix("0.5 * 15 + 2 * 10" )
    print(prefix.infix())
    print(prefix.prefix())
    print(prefix.arithmetic_expression_evaluation())
    
    print('-'*10)
    prefix = Prefix("( 12 + 7.5 ) * 3 - ( 0.1203 - 0.003 ) * ( 5 + 25 )")
    print(prefix.infix())
    print(prefix.prefix())
    print(prefix.arithmetic_expression_evaluation())
    
    print('-'*10)
    prefix = Prefix("3 + 4 - 5 ")
    print(prefix.infix())
    print(prefix.prefix())
    print(prefix.arithmetic_expression_evaluation())

    print('-'*10)
    prefix = Prefix("3 + 2 *4 ")
    print(prefix.infix())
    print(prefix.prefix())
    print(prefix.arithmetic_expression_evaluation())

    print('-'*10)
    prefix = Prefix("(3 + 2) *4 ")
    print(prefix.infix())
    print(prefix.prefix())
    print(prefix.arithmetic_expression_evaluation())

    print('-'*10)
    prefix = Prefix("3 + 4 * (5 - 2)")
    print(prefix.infix())
    print(prefix.prefix())
    print(prefix.arithmetic_expression_evaluation())

    print('-'*10)
    prefix = Prefix("7 * 3 - 6 / 2 + 4 ^ 2")
    print(prefix.infix())
    print(prefix.prefix())
    print(prefix.arithmetic_expression_evaluation())   

    print('-'*10)
    prefix = Prefix("(3^2 - 2 * 3 + 8 / 2)^2")
    print(prefix.infix())
    print(prefix.prefix())
    print(prefix.arithmetic_expression_evaluation())   

    print('-'*10)
    prefix = Prefix("4 ^ 3 ^ 2 ^ 1")
    print(prefix.infix())
    print(prefix.prefix())
    print(prefix.arithmetic_expression_evaluation())
