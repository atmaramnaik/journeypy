from journeypy.core.data.value import ValueHolder
from journeypy.core.data.variable import MapVariable, ValueHolderVariable


class Template(object):
    def process(self, context, io):
        map_variable = self.get_required_variables_blind(context)
        context.pour(map_variable.read(io))
        return self.fill(context)

    def get_required_variables_blind(self, context):
        return MapVariable({})

    def fill_return_value(self, context):
        pass

    def fill(self, context):
        return ValueHolder.get_new_value_holder_for(self.fill_return_value(context))

    def get_required_variables(self, context, io):
        if io is None:
            return self.get_required_variables_blind(context)
        return MapVariable({})


class Expression(object):
    def fill(self, context):
        pass

    def get_required_variables(self, context):
        pass


class ConstantExpression(Expression):
    def __init__(self, value):
        self.value = value

    def fill(self, context):
        return ValueHolder.get_new_value_holder_for(self.value)

    def get_required_variables(self,context):
        map_variable = MapVariable({})
        return map_variable


class VariableExpression(Expression):
    def __init__(self, name, data_type=type(None)):
        self.name = name
        self.type = data_type

    def of_type(self, data_type):
        self.type = data_type
        return self

    def fill(self, context):
        data=context.get(self.name)
        return ValueHolder.get_new_value_holder_for(data)

    def get_required_variables(self,context):
        map_variable = MapVariable({})

        if not self.name in context.currentContext:
            value_holder_type = ValueHolder.get_appropriate_value_holder(self.type)
            value_holder_variable = ValueHolderVariable(value_holder_type)
            map_variable.variable_map[self.name] = value_holder_variable

        return map_variable


class FunctionExpression(Expression):
    def __init__(self, operation, expressions=[]):
        self.operation = operation
        self.expressions = expressions

    def with_argument(self, expression):
        self.expressions.append(expression)
        return self

    def fill(self, context):
        lst_vh = []
        for expression in self.expressions:
            lst_vh.append(expression.fill(context))
        val = self.operation(*lst_vh)
        if isinstance(val,ValueHolder):
            return val
        else:
            return ValueHolder.get_new_value_holder_for(val)

    def get_required_variables(self, context):
        map_variable = MapVariable({})
        for expression in self.expressions:
            map_variable.variable_map.update(expression.get_required_variables(context).variable_map)

        return map_variable
