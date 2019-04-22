from journeypy.template.text.Templates import *
from journeypy.template.Expressions import *


def text(*argv):
    text_obj = Text()
    text_obj.blocks = argv
    return text_obj


def string(string_data):
    return StaticStringBlock(string_data)


def str_exp(expression):
    return ExpressionBlock(expression)


def var(name):
    return VariableExpression(name)


def fun(operation, *expressions):
    return FunctionExpression(operation, expressions)
