from journeypy.core.data.runtime import Context
from journeypy.template import VariableExpression, FunctionExpression, ConstantExpression, Expression
from journeypy.core.data.value import StringHolder,IntegerHolder
from journeypy.core.data.variable import MapVariable,ValueHolderVariable
import functools


# get_required_variables
def test_expression_get_required_variables():
    context = Context()
    exp = Expression()
    assert exp.get_required_variables(context) is None


def test_variable_expression_get_required_variables_when_in_context_str_var():
    context = Context()
    context.currentContext["name"] = "Atmaram"
    var_e = VariableExpression("name").of_type(str)
    val = var_e.get_required_variables(context)
    assert type(val) == MapVariable
    assert len(val.variable_map) == 0


def test_variable_expression_get_required_variables_when_not_in_context_str_var():
    context = Context()
    var_e = VariableExpression("name").of_type(str)
    val = var_e.get_required_variables(context)
    assert type(val) == MapVariable
    assert 'name' in val.variable_map
    var = val.variable_map['name']
    assert type(var) == ValueHolderVariable
    assert var.valueHolderClass == StringHolder


def test_variable_expression_get_required_variables_when_in_context_int_var():
    context = Context()
    context.currentContext["name"] = 123
    var_e = VariableExpression("name").of_type(int)
    val = var_e.get_required_variables(context)
    assert type(val) == MapVariable
    assert len(val.variable_map) == 0


def test_variable_expression_get_required_variables_when_not_in_context_int_var():
    context = Context()
    var_e = VariableExpression("name").of_type(int)
    val = var_e.get_required_variables(context)
    assert type(val) == MapVariable
    assert 'name' in val.variable_map
    var = val.variable_map['name']
    assert type(var) == ValueHolderVariable
    assert var.valueHolderClass == IntegerHolder


def test_constant_expression_get_required_variables_str_val():
    context = Context()
    var_e = ConstantExpression("Atmaram")
    val = var_e.get_required_variables(context)
    assert type(val) == MapVariable
    assert len(val.variable_map) == 0


def test_constant_expression_get_required_variables_int_val():
    context = Context()
    var_e = ConstantExpression(123)
    val = var_e.get_required_variables(context)
    assert type(val) == MapVariable
    assert len(val.variable_map) == 0


def test_function_expression_get_required_variables_when_in_context_str_var():
    context = Context()
    context.currentContext["name"] = "Atmaram"
    fun_e = FunctionExpression(join, [VariableExpression("name").of_type(str)])
    val = fun_e.get_required_variables(context)
    assert type(val) == MapVariable
    assert len(val.variable_map) == 0


def test_function_expression_get_required_variables_when_not_in_context_str_var():
    context = Context()
    fun_e = FunctionExpression(join, [VariableExpression("name").of_type(str)])
    val = fun_e.get_required_variables(context)
    assert type(val) == MapVariable
    assert 'name' in val.variable_map
    var = val.variable_map['name']
    assert type(var) == ValueHolderVariable
    assert var.valueHolderClass == StringHolder


def test_function_expression_get_required_variables_when_in_context_int_var():
    context = Context()
    context.currentContext["name"] = 123
    fun_e = FunctionExpression(add, [VariableExpression("name").of_type(int)])
    val = fun_e.get_required_variables(context)
    assert type(val) == MapVariable
    assert len(val.variable_map) == 0


def test_function_expression_get_required_variables_when_not_in_context_int_var():
    context = Context()
    fun_e = FunctionExpression(add, [VariableExpression("name").of_type(int)])
    val = fun_e.get_required_variables(context)
    assert type(val) == MapVariable
    assert 'name' in val.variable_map
    var = val.variable_map['name']
    assert type(var) == ValueHolderVariable
    assert var.valueHolderClass == IntegerHolder


# fill
def join(*args):
    return "".join(map(lambda x: str(x), args))


def add(*args):
    return functools.reduce(lambda x, y: x + y, args)


def test_expression_fill():
    context = Context()
    exp = Expression()
    assert exp.fill(context) is None


def test_variable_expression_fill_with_str():
    context = Context()
    context.currentContext["name"] = "Atmaram"
    var_e = VariableExpression("name").of_type(str)
    val = var_e.fill(context)
    assert type(val) == StringHolder
    assert val.value == "Atmaram"


def test_variable_expression_fill_with_int():
    context = Context()
    context.currentContext["name"] = 123
    var_e = VariableExpression("name").of_type(int)
    val = var_e.fill(context)
    assert type(val) == IntegerHolder
    assert val.value == 123


def test_variable_expression_fill_with_str_without_type():
    context = Context()
    context.currentContext["name"] = "Atmaram"
    var_e = VariableExpression("name")
    val = var_e.fill(context)
    assert type(val) == StringHolder
    assert val.value == "Atmaram"


def test_variable_expression_fill_with_int_without_type():
    context = Context()
    context.currentContext["name"] = 123
    var_e = VariableExpression("name")
    val = var_e.fill(context)
    assert type(val) == IntegerHolder
    assert val.value == 123


def test_constant_expression_fill_with_str():
    context=Context()
    fun_e = ConstantExpression("Atmaram")
    val = fun_e.fill(context)
    assert type(val) == StringHolder
    assert val.value == "Atmaram"


def test_constant_expression_fill_with_int():
    context=Context()
    fun_e = ConstantExpression(123)
    val = fun_e.fill(context)
    assert type(val) == IntegerHolder
    assert val.value == 123


def test_function_expression_fill_with_strings():
    context=Context()
    context.currentContext["name"] = "Atmaram"
    context.currentContext["place"] = "Pune"
    fun_e = FunctionExpression(join, [VariableExpression("name").of_type(str)]).with_argument(VariableExpression("place").of_type(str))
    val = fun_e.fill(context)
    assert val.value == "AtmaramPune"


def test_function_expression_fill_with_string_and_integer():
    context = Context()
    context.currentContext["name"] = "Atmaram"
    context.currentContext["place"] = 123
    fun_e = FunctionExpression(join, [VariableExpression("name").of_type(str), VariableExpression("place").of_type(int)])
    val = fun_e.fill(context)
    assert val.value == "Atmaram123"


def test_function_expression_fill_with_integer_and_integer():
    context = Context()
    context.currentContext["name"] = 123
    context.currentContext["place"] = 123
    fun_e = FunctionExpression(join, [VariableExpression("name").of_type(int), VariableExpression("place").of_type(int)])
    val = fun_e.fill(context)
    assert val.value == "123123"


def test_function_add_expression_fill_with_integer_and_integer():
    context = Context()
    context.currentContext["name"] = 123
    context.currentContext["place"] = 123
    fun_e = FunctionExpression(add, [VariableExpression("name").of_type(int), VariableExpression("place").of_type(int)])
    val = fun_e.fill(context)
    assert val.value == 246


def test_function_add_expression_fill_with_integer_and_string():
    context = Context()
    context.currentContext["name"] = 123
    context.currentContext["place"] = '123'
    fun_e = FunctionExpression(add, [VariableExpression("name").of_type(int), VariableExpression("place").of_type(str)])
    val = fun_e.fill(context)
    assert val.value == "123123"

