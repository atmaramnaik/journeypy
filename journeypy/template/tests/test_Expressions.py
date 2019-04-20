from journeypy.core.data.runtime.Context import Context
from journeypy.template.Expressions import *
import functools
def join(*args):
    return "".join(map(lambda x: str(x), args))

def add(*args):
    return functools.reduce(lambda x,y: x + y, args)

def test_function_expression_with_strings():
    context=Context()
    context.currentContext["name"]="Atmaram"
    context.currentContext["place"] = "Pune"
    funE=FunctionExpression(join,[VariableExpression("name").ofType(str),VariableExpression("place").ofType(str)])
    val=funE.fill(context)
    assert val.value=="AtmaramPune"

def test_function_expression_with_string_and_integer():
    context=Context()
    context.currentContext["name"]="Atmaram"
    context.currentContext["place"] = 123
    funE=FunctionExpression(join,[VariableExpression("name").ofType(str),VariableExpression("place").ofType(int)])
    val=funE.fill(context)
    assert val.value=="Atmaram123"

def test_function_expression_with_integer_and_integer():
    context=Context()
    context.currentContext["name"]=123
    context.currentContext["place"] = 123
    funE=FunctionExpression(join,[VariableExpression("name").ofType(int),VariableExpression("place").ofType(int)])
    val=funE.fill(context)
    assert val.value=="123123"

def test_function_add_expression_with_integer_and_integer():
    context=Context()
    context.currentContext["name"]=123
    context.currentContext["place"] = 123
    funE=FunctionExpression(add,[VariableExpression("name").ofType(int),VariableExpression("place").ofType(int)])
    val=funE.fill(context)
    assert val.value==246

def test_function_add_expression_with_integer_and_string():
    context=Context()
    context.currentContext["name"]=123
    context.currentContext["place"] = '123'
    funE=FunctionExpression(add,[VariableExpression("name").ofType(int),VariableExpression("place").ofType(str)])
    val=funE.fill(context)
    assert val.value=="123123"
