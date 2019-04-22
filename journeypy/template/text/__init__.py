from journeypy.core.data.variable import MapVariable
from journeypy.template import Template


class Text(Template):
    blocks = []

    def process(self, context, io):
        map_variable = self.get_required_variables(context, io)
        context.pour(map_variable.read(io))
        return self.fill(context)

    def get_required_variables_blind(self, context):
        map_variable = MapVariable({})
        return map_variable

    def fill_return_value(self, context):
        final_str = ''
        for block in self.blocks:
            final_str += block.fill(context)
        return final_str

    def get_required_variables(self, context, io):
        map_variable = MapVariable({})
        for block in self.blocks:
            map_variable.variable_map.update(block.get_required_variables(context).variable_map)

        return map_variable


class Block(object):
    def fill(self, context):
        pass

    def get_required_variables(self, context):
        pass

    def get_required_variables(self, context, io):
        return self.getRequiredVariables(self, context)


class StaticStringBlock(Block):
    value = None

    def __init__(self,value):
        self.value=value

    def fill(self,context):
        return self.value

    def get_required_variables(self,context):
        return MapVariable({})


class ExpressionBlock(Block):
    def __init__(self, expression):
        self.expression = expression

    def fill(self, context):
        return self.expression.fill(context).serialize()

    def get_required_variables(self, context):
        return self.expression.get_required_variables(context)
