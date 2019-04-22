from journeypy.core.data.runtime.Context import Context
from journeypy.template.Expressions import *
import functools


def join(*args):
    return "".join(map(lambda x: str(x), args))


def add(*args):
    return functools.reduce(lambda x, y: x + y, args)


def test_function_expression_with_strings():
    context=Context()
    context.currentContext["name"] = "Atmaram"
    context.currentContext["place"] = "Pune"
    fun_e = FunctionExpression(join, [VariableExpression("name").of_type(str), VariableExpression("place").of_type(str)])
    val = fun_e.fill(context)
    assert val.value == "AtmaramPune"


def test_function_expression_with_string_and_integer():
    context = Context()
    context.currentContext["name"] = "Atmaram"
    context.currentContext["place"] = 123
    fun_e = FunctionExpression(join, [VariableExpression("name").of_type(str), VariableExpression("place").of_type(int)])
    val = fun_e.fill(context)
    assert val.value == "Atmaram123"


def test_function_expression_with_integer_and_integer():
    context = Context()
    context.currentContext["name"] = 123
    context.currentContext["place"] = 123
    fun_e = FunctionExpression(join, [VariableExpression("name").of_type(int), VariableExpression("place").of_type(int)])
    val = fun_e.fill(context)
    assert val.value == "123123"


def test_function_add_expression_with_integer_and_integer():
    context = Context()
    context.currentContext["name"] = 123
    context.currentContext["place"] = 123
    fun_e = FunctionExpression(add, [VariableExpression("name").of_type(int), VariableExpression("place").of_type(int)])
    val = fun_e.fill(context)
    assert val.value == 246


def test_function_add_expression_with_integer_and_string():
    context = Context()
    context.currentContext["name"] = 123
    context.currentContext["place"] = '123'
    fun_e = FunctionExpression(add, [VariableExpression("name").of_type(int), VariableExpression("place").of_type(str)])
    val = fun_e.fill(context)
    assert val.value == "123123"
