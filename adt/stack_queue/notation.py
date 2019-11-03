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
        self.operators = {"+": 0, "-": 0, "*": 1, "/": 1, "^": 2, ")": 3, "(": 4}
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
        expression_postfix = ""

        # Place Parenthesis

        return expression_postfix

    def arithmetic_expression_evaluation(self) -> float:
        """
        Evaluación de la expresión aritmética en notación Postfix,
        utilizando una Stack, calculando el resultado final de la expresión.
        """
        result = 0

        return result

    def __verify_expression(self, expression: str) -> bool:
        expression = self.__format_expression(expression)

        # Verify Characters
        numbers = [str(i) for i in range(10)]
        for i in expression:
            if i not in self.operators and i not in ". " and i not in numbers:
                raise Exception(f"Invalid character: {i}")
                return False

        # Verify Order
        while " " in expression:
            expression = expression.replace(" ", "")
        expression = ' '.join(expression)
        expression = expression.split(' ')

        for i in range(len(expression)):
            try:
                bad_order = (
                    (expression[i] in '+-*/^(.' and expression[i + 1] in '+*/^).')
                    or (expression[i] == '(' and expression[i + 1] == '-')
                )
            except:
                bad_order = False
            if bad_order:
                raise Exception("Bad order of operators, parenthesis or dots")
                return not bad_order

        # Balanced Parenthesis
        stack = Stack()
        err = False
        for i in expression:
            if i == '(':
                stack.push(i)
            elif i == ')':
                if stack.is_empty():
                    err = True
                    break
                stack.pop()

        if err or not stack.is_empty():
            raise Exception('The parenthesis are not balanced')
            return False

        return True

    def __format_expression(self, expression: str) -> str:
        # Remove spaces
        expression = expression.strip()
        while " " in expression:
            expression = expression.replace(" ", "")

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
