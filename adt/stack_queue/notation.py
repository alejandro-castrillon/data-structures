from adt.lists.sll import SinglyLinkedList
from adt.stack_queue.stack import Stack


class Postfix:
    """
    Clase que implementa la transformación de un expresión
    matemática Infix a Postfix (Reverse Polish notation) y el
    cálculo de la expresión aritmética Postfix.
    Los operandos utilizados serán de cualquier cantidad de
    dígitos.
    Operadores Válidos:
    + : Suma
    - : Resta
    * : Multiplicación
    / : División
    ^ : Potenciación
    ( : Paréntesis Izquierdo
    ) : Paréntesis Derecho
    """

    def __init__(self, expresión_infix: str) -> None:
        if self.__verify_expression(expresión_infix):
            self.expression_infix = self.__format_expression(expresión_infix)

    def infix(self) -> str:
        """
        Método que retorna la expresión Infix original, separando cada
        operando y cada operador, incluyendo los paréntesis, por un espacio
        en blanco.
        """
        return self.expression_infix

    def postfix(self) -> str:
        """
        Método que convierte una expresión Infix a una expresión Postfix,
        haciendo uso de una Stack. Separar operandos y operadores por un
        espacio en blanco.
        """
        priorities = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, ')': 4}
        operators_stack = Stack()

        infix_list = self.__split(self.expression_infix, ' ')
        postfix_list = SinglyLinkedList()

        for i in infix_list:
            try:
                _ = float(i)
                postfix_list.append(i)
                continue
            except:
                pass
            if i == '(':
                while operators_stack.peek() != ')' and not operators_stack.is_empty():
                    postfix_list.append(operators_stack.pop())
            elif i in priorities:
                if operators_stack.is_empty():
                    operators_stack.push(i)
                else:
                    top = operators_stack.pop()
                    if priorities[i] >= priorities[top] or top == ')':
                        operators_stack.push(top)
                    else:
                        postfix_list.append(top)
                        while operators_stack.peek() != ')' and not operators_stack.is_empty():
                            postfix_list.append(operators_stack.pop())
                    operators_stack.push(i)

        while not operators_stack.is_empty():
            postfix_list.append(operators_stack.pop())

        expression_postfix = ''
        for i in postfix_list:
            expression_postfix += str(i) + ' '

        return expression_postfix[:len(expression_postfix) - 1]

    def arithmetic_expression_evaluation(self) -> float:
        """
        Evaluación de la expresión aritmética en notación Postfix,
        utilizando una Stack, calculando el resultado final de la expresión.
        """
        result = 0

        return result

    def __verify_expression(self, expression: str) -> bool:
        verify_characters = self.__verify_characters(expression)
        verify_operators = self.__verify_operators(expression)
        balanced_parenthesis = self.__balanced_parenthesis(expression)

        return verify_characters and verify_operators and balanced_parenthesis

    def __verify_characters(self, expression: str):
        expression = self.__remove_spaces(expression)
        for i in expression:
            if i not in '+-*/^().' and not i.isdigit():
                raise Exception(f"Invalid character: {i}")
                return False
        return True

    def __verify_operators(self, expression):
        expression = self.__remove_spaces(expression)

        for i in range(len(expression)):
            try:
                bad_order = (
                    (expression[i] in '+-*/^(.' and expression[i + 1] in '+*/^).')
                    or (expression[i] == '(' and expression[i + 1] == '-')
                    or expression[0] in '+*/^).'
                    or expression[len(expression)] in '+*/^(.'
                )
            except:
                bad_order = False
            if bad_order:
                raise Exception(
                    f"Bad order of operators, parenthesis or dots at character {i}"
                )
                return not bad_order
        return True

    def __balanced_parenthesis(self, expression: str):
        stack = Stack()
        error = False
        for i in expression:
            if i == '(':
                stack.push(i)
            elif i == ')':
                if stack.is_empty():
                    error = True
                    break
                stack.pop()
        if error or not stack.is_empty():
            raise Exception('The parenthesis are not balanced')
            return False
        return True

    def __format_expression(self, expression: str) -> str:
        expression = self.__remove_spaces(expression)

        # Separate Characters
        array = " ".join(expression)
        expression = ""
        for i in array:
            expression += i

        # Unite Numbers
        for i in range(len(expression)):
            try:
                if expression[i].isdigit() and expression[i + 2].isdigit():
                    expression = expression[: i + 1] + expression[i + 2 :]
            except:
                pass

        # Unite Decimals
        while " . " in expression:
            expression = expression.replace(" . ", ".")

        return expression

    def __remove_spaces(self, expression):
        expression = expression.strip()
        while " " in expression:
            expression = expression.replace(" ", "")
        return expression

    def __split(self, string: str, char=''):
        _list = SinglyLinkedList()
        if char:
            while char in string:
                index = string.find(char)
                _list.append(string[: index])
                string = string[index + 1 :]
            _list.append(string)
        else:
            for i in string:
                _list.append(i)
        return _list


class Prefix:
    """
    Clase que implementa la transformación de un expresión
    matemática Infix a Prefix (Polish notation) y el cálculo de
    la expresión aritmética Prefix.
    Los operandos utilizados serán de cualquier cantidad de
    dígitos.
    Operadores Válidos:
    + : Suma
    - : Resta
    * : Multiplicación
    / : División
    ^ : Potenciación
    ( : Paréntesis Izquierdo
    """

    def __init__(self, infix_expression: str) -> None:
        pass

    def infix(self) -> str:
        """
        Método que retorna la expresión Infix original, separando cada
        operando y cada operador, incluyendo los paréntesis, por un espacio
        en blanco.
        """
        pass

    def prefix(self) -> str:
        """
        Método que convierte una expresión Infix a una expresión Prefix,
        haciendo uso de una Stack. Separar operandos y operadores por un
        espacio en blanco.
        """
        pass

    def arithmetic_expression_evaluation(self) -> float:
        """
        Evaluación de la expresión aritmética en notación Prefix, utilizando
        una Stack, calculando el resultado final de la expresión.
        """
        pass
