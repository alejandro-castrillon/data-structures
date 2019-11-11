#!/usr/bin/env python3
"""
    MODULE: test_notaciones.py
    DESCRIPTION:
    DATE: 19.05.2019 18:23:01 COT
"""
import sys

# *****************************************************************************
# sys.path.append(
#     "/home/jacques/+ Clases EDI/+ Prácticas (Python)/p03_pilas_colas")
# *****************************************************************************
sys.path.append("/home/jacques/+ Clases EDI/+ Talleres/T4c/PRE_FIJ/1")
from adt.stack_queue.notation import Prefix
from adt.stack_queue.notation import Postfix

dict_pruebas = {
    "Prefix": 0,
    "Prefix_chica": 0,
    "postfix": 10,
    "postfix_chica": 0,
}


def prueba_Prefix():
    fNota_P = 1.0 / 3
    # Prueba de una expresión aritmética sin paréntesis y espacios en blanco
    iFallas = 0
    print(
        "1) La Prueba de una expresión aritmética sin paréntesis y espacios "
        "en blanco es:"
    )
    eva_pref_exp1 = Prefix("5   + 6^ 2")
    try:
        assert (
            "5 + 6 ^ 2" == eva_pref_exp1.infix()
        ), "NO pasaste la prueba 1 infix"
        print("OK, pasaste la prueba 1 infix")
    except Exception as ae:
        iFallas += 1
        print(ae)
    try:
        assert (
            "+ 5 ^ 6 2" == eva_pref_exp1.prefix()
        ), "NO pasaste la prueba 1 Prefix"
        print("OK, pasaste la prueba 1 Prefix")
    except Exception as ae:
        iFallas += 1
        print(ae)
    try:
        assert (
            41.0 == eva_pref_exp1.arithmetic_expression_evaluation()
        ), "NO pasaste la prueba 1 arithmetic_expression_evaluation"
        print("OK, pasaste la prueba 1 arithmetic_expression_evaluation")
    except Exception as ae:
        iFallas += 1
        print(ae)
    print(
        "ATENCIÓN, Fallaste Prueba 1! (" + str(3 - iFallas) + "/3) Buenas"
        if iFallas > 0
        else "Todo OK, Prueba 1!"
    )
    fNota_P1 = round(fNota_P * (3 - iFallas), 3)
    print(f"Nota Prueba # 1 = {fNota_P1}")
    print("-" * 50)

    # Prueba de una expresión aritmética con paréntesis y espacios en blanco
    iFallas = 0
    print(
        "2) La Prueba de una expresión aritmética con paréntesis y espacios "
        "en blanco es:"
    )
    eva_pref_exp2 = Prefix("5*(35+6-(1/5 ^16 )- 7)-8")
    try:
        assert (
            "5 * ( 35 + 6 - ( 1 / 5 ^ 16 ) - 7 ) - 8" == eva_pref_exp2.infix()
        ), "NO pasaste la prueba 2 infix"
        print("OK, pasaste la prueba 2 infix")
    except Exception as ae:
        iFallas += 1
        print(ae)
    try:
        print(eva_pref_exp2.prefix(), "<->", "- * 5 - - + 35 6 / 1 ^ 5 16 7 8")
        assert (
            "- * 5 - - + 35 6 / 1 ^ 5 16 7 8" == eva_pref_exp2.prefix()
        ), "NO pasaste la prueba 2 Prefix"
        print("OK, pasaste la prueba 2 Prefix")
    except Exception as ae:
        iFallas += 1
        print(ae)
    try:
        assert (
            161.99999999996726
            == eva_pref_exp2.arithmetic_expression_evaluation()
        ), "NO pasaste la prueba 2 arithmetic_expression_evaluation"
        print("OK, pasaste la prueba 2 arithmetic_expression_evaluation")
    except Exception as ae:
        iFallas += 1
        print(ae)
    print(
        "ATENCIÓN, Fallaste Prueba 2! (" + str(3 - iFallas) + "/3) Buenas"
        if iFallas > 0
        else "Todo OK, Prueba 2!"
    )
    fNota_P2 = round(fNota_P * (3 - iFallas), 3)
    print(f"Nota Prueba # 2 = {fNota_P2}")
    print("-" * 50)

    # Prueba de una expresión aritmética con varios paréntesis
    iFallas = 0
    print("3) La Prueba de una expresión aritmética con varios paréntesis es:")
    eva_pref_exp3 = Prefix("((15 / (7 - (1+1)))* 3)- (2 + (1 + 1))")
    try:
        assert (
            "( ( 15 / ( 7 - ( 1 + 1 ) ) ) * 3 ) - ( 2 + ( 1 + 1 ) )"
            == eva_pref_exp3.infix()
        ), "NO pasaste la prueba 3 infix"
        print("OK, pasaste la prueba 3 infix")
    except Exception as ae:
        iFallas += 1
        print(ae)
    try:
        assert (
            "- * / 15 - 7 + 1 1 3 + 2 + 1 1" == eva_pref_exp3.prefix()
        ), "NO pasaste la prueba 3 Prefix"
        print("OK, pasaste la prueba 3 Prefix")
    except Exception as ae:
        iFallas += 1
        print(ae)
    try:
        assert (
            5.0 == eva_pref_exp3.arithmetic_expression_evaluation()
        ), "NO pasaste la prueba 3 arithmetic_expression_evaluation"
        print("OK, pasaste la prueba 3 arithmetic_expression_evaluation")
    except Exception as ae:
        iFallas += 1
        print(ae)
    print(
        "ATENCIÓN, Fallaste Prueba 3! (" + str(3 - iFallas) + "/3) Buenas"
        if iFallas > 0
        else "Todo OK, Prueba 3!"
    )
    fNota_P3 = round(fNota_P * (3 - iFallas), 3)
    print(f"Nota Prueba # 3 = {fNota_P3}")
    print("-" * 50)

    # Prueba de una expresión aritmética con Operandos de varios dígitos
    iFallas = 0
    print(
        "4) La Prueba de una expresión aritmética con Operandos de varios "
        "dígitos es:"
    )
    eva_pref_exp4 = Prefix("(11/7) ^3* ( 30564 - 4 ) +25 / 9- 3 * 10")
    try:
        assert (
            "( 11 / 7 ) ^ 3 * ( 30564 - 4 ) + 25 / 9 - 3 * 10"
            == eva_pref_exp4.infix()
        ), "NO pasaste la prueba 4 infix"
        print("OK, pasaste la prueba 4 infix")
    except Exception as ae:
        iFallas += 1
        print(ae)
    try:
        assert (
            "- + * ^ / 11 7 3 - 30564 4 / 25 9 * 3 10" == eva_pref_exp4.prefix()
        ), "NO pasaste la prueba 4 Prefix"
        print("OK, pasaste la prueba 4 Prefix")
    except Exception as ae:
        iFallas += 1
        print(ae)
    try:
        assert (
            118559.83317136379
            == eva_pref_exp4.arithmetic_expression_evaluation()
        ), "NO pasaste la prueba 4 arithmetic_expression_evaluation"
        print("OK, pasaste la prueba 4 arithmetic_expression_evaluation")
    except Exception as ae:
        iFallas += 1
        print(ae)
    print(
        "ATENCIÓN, Fallaste Prueba 4! (" + str(3 - iFallas) + "/3) Buenas"
        if iFallas > 0
        else "Todo OK, Prueba 4!"
    )
    fNota_P4 = round(fNota_P * (3 - iFallas), 3)
    print(f"Nota Prueba # 4 = {fNota_P4}")
    print("-" * 50)

    # Prueba de una expresión aritmética evaluada de Derecha a Izquierada con ^
    iFallas = 0
    print(
        "5) La Prueba de una expresión aritmética evaluada de Derecha a "
        "Izquierda con ^ es:"
    )
    eva_pref_exp5 = Prefix("2^ 3 ^4^ 1")
    try:
        assert (
            "2 ^ 3 ^ 4 ^ 1" == eva_pref_exp5.infix()
        ), "NO pasaste la prueba 5 infix"
        print("OK, pasaste la prueba 5 infix")
    except Exception as ae:
        iFallas += 1
        print(ae)
    try:
        assert (
            "^ 2 ^ 3 ^ 4 1" == eva_pref_exp5.prefix()
        ), "NO pasaste la prueba 5 Prefix"
        print("OK, pasaste la prueba 5 Prefix")
    except Exception as ae:
        iFallas += 1
        print(ae)
    try:
        assert (
            2.4178516392292583e24
            == eva_pref_exp5.arithmetic_expression_evaluation()
        ), "NO pasaste la prueba 5 arithmetic_expression_evaluation"
        print("OK, pasaste la prueba 5 arithmetic_expression_evaluation")
    except Exception as ae:
        iFallas += 1
        print(ae)
    print(
        "ATENCIÓN, Fallaste Prueba 5! (" + str(3 - iFallas) + "/3) Buenas"
        if iFallas > 0
        else "Todo OK, Prueba 5!"
    )
    fNota_P5 = round(fNota_P * (3 - iFallas), 3)
    print(f"Nota Prueba # 5 = {fNota_P5}")
    print("-" * 50)
    print("=" * 20)
    print(f"NOTA: {fNota_P1 + fNota_P2 + fNota_P3 + fNota_P4 + fNota_P5}")
    print("=" * 20)


def prueba_postfix():
    fNota_P = 1.0 / 3
    # Prueba de una expresión aritmética sin paréntesis y espacios en blanco
    iFallas = 0
    print(
        "1) La Prueba de una expresión aritmética sin paréntesis y espacios "
        "en blanco es:"
    )
    eva_exp_posfj1 = Postfix("5 +   6 ^2")
    try:
        assert (
            "5 + 6 ^ 2" == eva_exp_posfj1.infix()
        ), "NO pasaste la prueba 1 infix"
        print("OK, pasaste la prueba 1 infix")
    except Exception as ae:
        iFallas += 1
        print(ae)
    try:
        assert (
            "5 6 2 ^ +" == eva_exp_posfj1.postfix()
        ), "NO pasaste la prueba 1 postfix"
        print("OK, pasaste la prueba 1 postfix")
    except Exception as ae:
        iFallas += 1
        print(ae)
    try:
        assert (
            41.0 == eva_exp_posfj1.arithmetic_expression_evaluation()
        ), "NO pasaste la prueba 1 arithmetic_expression_evaluation"
        print("OK, pasaste la prueba 1 arithmetic_expression_evaluation")
    except Exception as ae:
        iFallas += 1
        print(ae)
    print(
        "ATENCIÓN, Fallaste Prueba 1! (" + str(3 - iFallas) + "/3) Buenas"
        if iFallas > 0
        else "Todo OK, Prueba 1!"
    )
    fNota_P1 = round(fNota_P * (3 - iFallas), 3)
    print(f"Nota Prueba # 1 = {fNota_P1}")
    print("-" * 50)

    # Prueba de una expresión aritmética con paréntesis y espacios en blanco
    iFallas = 0
    print(
        "2) La Prueba de una expresión aritmética con paréntesis y espacios "
        "en blanco es:"
    )
    eva_exp_posfj2 = Postfix("5*(35+6-(1/5^ 16 )- 7)-8")
    try:
        assert (
            "5 * ( 35 + 6 - ( 1 / 5 ^ 16 ) - 7 ) - 8" == eva_exp_posfj2.infix()
        ), "NO pasaste la prueba 2 infix"
        print("OK, pasaste la prueba 2 infix")
    except Exception as ae:
        iFallas += 1
        print(ae)
    try:
        assert (
            "5 35 6 + 1 5 16 ^ / - 7 - * 8 -" == eva_exp_posfj2.postfix()
        ), "NO pasaste la prueba 2 postfix"
        print("OK, pasaste la prueba 2 postfix")
    except Exception as ae:
        iFallas += 1
        print(ae)
    try:
        assert (
            161.99999999996726
            == eva_exp_posfj2.arithmetic_expression_evaluation()
        ), "NO pasaste la prueba 2 arithmetic_expression_evaluation"
        print("OK, pasaste la prueba 2 arithmetic_expression_evaluation")
    except Exception as ae:
        iFallas += 1
        print(ae)
    print(
        "ATENCIÓN, Fallaste Prueba 2! (" + str(3 - iFallas) + "/3) Buenas"
        if iFallas > 0
        else "Todo OK, Prueba 2!"
    )
    fNota_P2 = round(fNota_P * (3 - iFallas), 3)
    print(f"Nota Prueba # 2 = {fNota_P2}")
    print("-" * 50)

    # Prueba de una expresión aritmética con varios paréntesis
    iFallas = 0
    print("3) La Prueba de una expresión aritmética con varios paréntesis es:")
    eva_exp_posfj3 = Postfix("(( 15 / (7 - (1+1)))* 3)-  (2 + (1 + 1))")
    try:
        assert (
            "( ( 15 / ( 7 - ( 1 + 1 ) ) ) * 3 ) - ( 2 + ( 1 + 1 ) )"
            == eva_exp_posfj3.infix()
        ), "NO pasaste la prueba 3 infix"
        print("OK, pasaste la prueba 3 infix")
    except Exception as ae:
        iFallas += 1
        print(ae)
    try:
        assert (
            "15 7 1 1 + - / 3 * 2 1 1 + + -" == eva_exp_posfj3.postfix()
        ), "NO pasaste la prueba 3 postfix"
        print("OK, pasaste la prueba 3 postfix")
    except Exception as ae:
        iFallas += 1
        print(ae)
    try:
        assert (
            5.0 == eva_exp_posfj3.arithmetic_expression_evaluation()
        ), "NO pasaste la prueba 3 arithmetic_expression_evaluation"
        print("OK, pasaste la prueba 3 arithmetic_expression_evaluation")
    except Exception as ae:
        iFallas += 1
        print(ae)
    print(
        "ATENCIÓN, Fallaste Prueba 3! (" + str(3 - iFallas) + "/3) Buenas"
        if iFallas > 0
        else "Todo OK, Prueba 3!"
    )
    fNota_P3 = round(fNota_P * (3 - iFallas), 3)
    print(f"Nota Prueba # 3 = {fNota_P3}", (12 - 800) ^ 3 + 7)
    print("-" * 50)

    # Prueba de una expresión aritmética con Operandos de varios dígitos
    iFallas = 0
    print(
        "4) La Prueba de una expresión aritmética con Operandos de varios "
        "dígitos es:"
    )
    eva_exp_posfj4 = Postfix("(11/7) ^3 * ( 30564 - 4 ) +25 / 9- 3 * 10")
    try:
        assert (
            "( 11 / 7 ) ^ 3 * ( 30564 - 4 ) + 25 / 9 - 3 * 10"
            == eva_exp_posfj4.infix()
        ), "NO pasaste la prueba 4 infix"
        print("OK, pasaste la prueba 4 infix")
    except Exception as ae:
        iFallas += 1
        print(ae)
    try:
        assert (
            "11 7 / 3 ^ 30564 4 - * 25 9 / + 3 10 * -"
            == eva_exp_posfj4.postfix()
        ), "NO pasaste la prueba 4 postfix"
        print("OK, pasaste la prueba 4 postfix")
    except Exception as ae:
        iFallas += 1
        print(ae)
    try:
        assert (
            118559.83317136379
            == eva_exp_posfj4.arithmetic_expression_evaluation()
        ), "NO pasaste la prueba 4 arithmetic_expression_evaluation"
        print("OK, pasaste la prueba 4 arithmetic_expression_evaluation")
    except Exception as ae:
        iFallas += 1
        print(ae)
    print(
        "ATENCIÓN, Fallaste Prueba 4! (" + str(3 - iFallas) + "/3) Buenas"
        if iFallas > 0
        else "Todo OK, Prueba 4!"
    )
    fNota_P4 = round(fNota_P * (3 - iFallas), 3)
    print(f"Nota Prueba # 4 = {fNota_P4}")
    print("-" * 50)

    # Prueba de una expresión aritmética evaluada de Derecha a Izquierda con ^
    iFallas = 0
    print(
        "5) La Prueba de una expresión aritmética evaluada de Derecha a "
        "Izquierda con ^ es:"
    )
    eva_exp_posfj5 = Postfix("2 ^3^ 4^ 1")
    try:
        assert (
            "2 ^ 3 ^ 4 ^ 1" == eva_exp_posfj5.infix()
        ), "NO pasaste la prueba 5 infix"
        print("OK, pasaste la prueba 5 infix")

    # pila ^
    # post 2 3 ^

    except Exception as ae:
        iFallas += 1
        print(ae)
    try:
        assert (
            "2 3 4 1 ^ ^ ^" == eva_exp_posfj5.postfix()
        ), "NO pasaste la prueba 5 postfix"
        print("OK, pasaste la prueba 5 postfix")
    except Exception as ae:
        iFallas += 1
        print(ae)
    try:
        assert (
            2.4178516392292583e24
            == eva_exp_posfj5.arithmetic_expression_evaluation()
        ), "NO pasaste la prueba 5 arithmetic_expression_evaluation"
        print("OK, pasaste la prueba 5 arithmetic_expression_evaluation")
    except Exception as ae:
        iFallas += 1
        print(ae)
    print(
        "ATENCIÓN, Fallaste Prueba 5! (" + str(3 - iFallas) + "/3) Buenas"
        if iFallas > 0
        else "Todo OK, Prueba 5!"
    )
    fNota_P5 = round(fNota_P * (3 - iFallas), 3)
    print(f"Nota Prueba # 5 = {fNota_P5}")
    print("-" * 50)
    print("=" * 20)
    print(f"NOTA: {fNota_P1 + fNota_P2 + fNota_P3 + fNota_P4 + fNota_P5}")
    print("=" * 20)


def prueba_postfix_chica():
    expr_mat = "1+2*3^4-5*6/7"
    expr_mat = "4^3^2^1"
    eva_exp_posfj1 = Postfix(expr_mat)
    print(eva_exp_posfj1.infix())
    print(eva_exp_posfj1.postfix())
    print(eva_exp_posfj1.arithmetic_expression_evaluation())


def prueba_Prefix_chica():
    expr_mat = "4^3^2^1"
    eva_exp_prefj1 = Prefix(expr_mat)
    print(eva_exp_prefj1.infix())
    print(eva_exp_prefj1.prefix())
    print(eva_exp_prefj1.arithmetic_expression_evaluation())


if __name__ == "__main__":
    if dict_pruebas.get("Prefix"):
        if dict_pruebas.get("Prefix_chica"):
            prueba_Prefix_chica()
        else:
            prueba_Prefix()
    elif dict_pruebas.get("postfix"):
        if dict_pruebas.get("postfix_chica"):
            prueba_postfix_chica()
        else:
            prueba_postfix()
