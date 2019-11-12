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
        self.expression_infix = expresión_infix

    def infix(self) -> str:
        """
        Método que retorna la expresión Infix original, separando cada
        operando y cada operador, incluyendo los paréntesis, por un espacio
        en blanco.
        """
        if self.__verify_expression(self.expression_infix):
            self.expression_infix = self.__format_expression(
                self.expression_infix
            )
            return self.expression_infix

    def postfix(self) -> str:
        """
        Método que convierte una expresión Infix a una expresión Postfix,
        haciendo uso de una Stack. Separar operandos y operadores por un
        espacio en blanco.
        """
        priorities = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "(": 0}
        operators_stack = Stack()

        infix_list = self.__split(self.infix(), " ")
        postfix_list = SinglyLinkedList()

        for i in infix_list:
            if self.__isdigit(i):
                postfix_list.append(i)
            elif i == ")":
                top = operators_stack.pop()
                while top != "(" and not operators_stack.is_empty():
                    postfix_list.append(top)
                    top = operators_stack.pop()
            elif i == "(":
                operators_stack.push(i)
            elif i in priorities:
                if operators_stack.is_empty():
                    operators_stack.push(i)
                else:
                    top = operators_stack.peek()
                    if priorities[i] > priorities[top] or i == top == "^":
                        operators_stack.push(i)
                    else:
                        while not operators_stack.is_empty():
                            top = operators_stack.peek()
                            if priorities[top] >= priorities[i]:
                                postfix_list.append(operators_stack.pop())
                            else:
                                break
                        operators_stack.push(i)

        while not operators_stack.is_empty():
            postfix_list.append(operators_stack.pop())

        expression_postfix = ""
        for i in postfix_list:
            expression_postfix += str(i) + " "

        return expression_postfix[: len(expression_postfix) - 1]

    def arithmetic_expression_evaluation(self) -> float:
        """
        Evaluación de la expresión aritmética en notación Postfix,
        utilizando una Stack, calculando el resultado final de la expresión.
        """
        result = None
        postfix_list = self.__split(self.postfix(), " ")
        operands_stack = Stack()

        for i in postfix_list:
            if self.__isdigit(i):
                operands_stack.push(i)
            elif i in "+-*/^":
                num2 = operands_stack.pop()
                num1 = operands_stack.pop()
                result = self.__operate(num1, num2, i)
                operands_stack.push(str(result))
        return result

    def __verify_expression(self, expression: str) -> bool:
        verify_characters = self.__verify_characters(expression)
        verify_operators = self.__verify_operators(expression)
        balanced_parenthesis = self.__balanced_parenthesis(expression)

        return verify_characters and verify_operators and balanced_parenthesis

    def __verify_characters(self, expression: str) -> bool:
        expression = self.__remove_spaces(expression)
        for i in expression:
            if i not in "+-*/^()." and not i.isdigit():
                return False
        return True

    def __verify_operators(self, expression: str) -> bool:
        expression = self.__remove_spaces(expression)
        for i in range(len(expression)):
            try:
                bad_order = (
                    (
                        expression[i] in "+-*/^(."
                        and expression[i + 1] in "+-*/^)."
                    )
                    or (expression[i].isdigit() and expression[i + 1] == '(')
                    or (expression[i] == ')' and expression[i + 1].isdigit())
                    or (expression[i] == ')' and expression[i + 1] == '(')
                    or (expression[i] == "(" and expression[i + 1] == "-")
                    or expression[0] in "+*/^)."
                    or expression[len(expression)] in "+*/^(."
                )
                if bad_order:
                    return not bad_order
            except:
                pass
        return True

    def __balanced_parenthesis(self, expression: str) -> bool:
        stack = Stack()
        error = False
        for i in expression:
            if i == "(":
                stack.push(i)
            elif i == ")":
                if stack.is_empty():
                    error = True
                    break
                stack.pop()
        if error or not stack.is_empty():
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
                if expression[i - 1].isdigit() and expression[i + 1].isdigit():
                    expression = expression[:i] + expression[i + 1 :]
            except:
                pass

        # Unite Decimals
        while " . " in expression:
            expression = expression.replace(" . ", ".")

        return expression

    def __remove_spaces(self, expression: str) -> str:
        expression = expression.strip()
        while " " in expression:
            expression = expression.replace(" ", "")
        return expression

    def __split(self, string: str, sep: str = "") -> SinglyLinkedList:
        splited_list = SinglyLinkedList()
        if sep:
            while sep in string:
                index = string.find(sep)
                splited_list.append(string[:index])
                string = string[index + 1 :]
            splited_list.append(string)
        else:
            for i in string:
                splited_list.append(i)
        return splited_list

    def __isdigit(self, string: str) -> bool:
        try:
            float(string)
            return True
        except:
            return False

    def __operate(self, operand1: str, operand2: str, operator: str) -> float:
        return {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
            "^": lambda a, b: a ** b,
        }[operator](float(operand1), float(operand2))


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
        self.infix_expression = infix_expression

    def infix(self) -> str:
        """
        Método que retorna la expresión Infix original, separando cada
        operando y cada operador, incluyendo los paréntesis, por un espacio
        en blanco.
        """
        if self.__verify_expression(self.infix_expression):
            self.infix_expression = self.__format_expression(
                self.infix_expression
            )
            return self.infix_expression

    def prefix(self) -> str:
        """
        Método que convierte una expresión Infix a una expresión Prefix,
        haciendo uso de una Stack. Separar operandos y operadores por un
        espacio en blanco.
        """
        priorities = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, ")": 4}
        operators_stack = Stack()

        infix_expression = self.__reverse_expression(self.infix_expression)
        infix_list = self.__split(infix_expression, " ")
        prefix_list = SinglyLinkedList()

        for i in infix_list:
            if self.__isdigit(i):
                prefix_list.append(i)
            elif i == "(":
                top = operators_stack.pop()
                while top != ")" and not operators_stack.is_empty():
                    prefix_list.append(top)
                    top = operators_stack.pop()
            elif i in priorities:
                if operators_stack.is_empty():
                    operators_stack.push(i)
                else:
                    top = operators_stack.peek()
                    if priorities[i] >= priorities[top] or top == ")":
                        if i == top == "^":
                            prefix_list.append(i)
                        else:
                            operators_stack.push(i)
                    else:
                        while not operators_stack.is_empty():
                            top = operators_stack.peek()
                            if priorities[top] > priorities[i] and top != ")":
                                prefix_list.append(operators_stack.pop())
                            else:
                                break
                        operators_stack.push(i)

        while not operators_stack.is_empty():
            prefix_list.append(operators_stack.pop())

        expression_prefix = ""
        for i in prefix_list:
            expression_prefix += str(i) + " "

        expression_prefix = expression_prefix[: len(expression_prefix) - 1]
        expression_prefix = self.__reverse_expression(expression_prefix)

        return expression_prefix

    def arithmetic_expression_evaluation(self) -> float:
        """
        Evaluación de la expresión aritmética en notación Prefix, utilizando
        una Stack, calculando el resultado final de la expresión.
        """
        result = None
        expression_prefix = self.__reverse_expression(self.prefix())
        postfix_list = self.__split(expression_prefix, " ")
        operands_stack = Stack()

        for i in postfix_list:
            if self.__isdigit(i):
                operands_stack.push(i)
            elif i in "+-*/^":
                num1 = operands_stack.pop()
                num2 = operands_stack.pop()
                result = self.__operate(num1, num2, i)
                operands_stack.push(str(result))
        return result

    def __verify_expression(self, expression: str) -> bool:
        verify_characters = self.__verify_characters(expression)
        verify_operators = self.__verify_operators(expression)
        balanced_parenthesis = self.__balanced_parenthesis(expression)

        return verify_characters and verify_operators and balanced_parenthesis

    def __verify_characters(self, expression: str) -> bool:
        expression = self.__remove_spaces(expression)
        for i in expression:
            if i not in "+-*/^()." and not i.isdigit():
                raise Exception(f"Invalid character: {i}")
                return False
        return True

    def __verify_operators(self, expression: str) -> bool:
        expression = self.__remove_spaces(expression)
        for i in range(len(expression)):
            try:
                bad_order = (
                    (
                        expression[i] in "+-*/^(."
                        and expression[i + 1] in "+-*/^)."
                    )
                    or (expression[i].isdigit() and expression[i + 1] == '(')
                    or (expression[i] == ')' and expression[i + 1].isdigit())
                    or (expression[i] == ')' and expression[i + 1] == '(')
                    or (expression[i] == "(" and expression[i + 1] == "-")
                    or expression[0] in "+*/^)."
                    or expression[len(expression)] in "+*/^(."
                )
                if bad_order:
                    return not bad_order
            except:
                pass
        return True

    def __balanced_parenthesis(self, expression: str) -> bool:
        stack = Stack()
        error = False
        for i in expression:
            if i == "(":
                stack.push(i)
            elif i == ")":
                if stack.is_empty():
                    error = True
                    break
                stack.pop()
        if error or not stack.is_empty():
            raise Exception("The parenthesis are not balanced")
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
                if expression[i - 1].isdigit() and expression[i + 1].isdigit():
                    expression = expression[:i] + expression[i + 1 :]
            except:
                pass

        # Unite Decimals
        while " . " in expression:
            expression = expression.replace(" . ", ".")

        return expression

    def __remove_spaces(self, expression: str) -> str:
        expression = expression.strip()
        while " " in expression:
            expression = expression.replace(" ", "")
        return expression

    def __split(self, expression: str, sep: str = "") -> SinglyLinkedList:
        splited_list = SinglyLinkedList()
        if sep:
            while sep in expression:
                index = expression.find(sep)
                splited_list.append(expression[:index])
                expression = expression[index + 1 :]
            splited_list.append(expression)
        else:
            for i in expression:
                splited_list.append(i)
        return splited_list

    def __isdigit(self, string: str) -> bool:
        try:
            float(string)
            return True
        except:
            return False

    def __operate(self, operand1: str, operand2: str, operator: str) -> float:
        return {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
            "^": lambda a, b: a ** b,
        }[operator](float(operand1), float(operand2))

    def __reverse_expression(self, expression: str) -> str:
        expression = self.__split(expression, " ")
        stack = Stack()
        for i in expression:
            stack.push(i)

        expression = ""
        while not stack.is_empty():
            expression += stack.pop() + " "

        return expression[: len(expression) - 1]
