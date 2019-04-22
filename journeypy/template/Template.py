from journeypy.core.data.value.Values import ValueHolder
from journeypy.core.data.variable.Variables import MapVariable
class Template(object):
    def process(self, context, io):
        map_variable=self.get_required_variables_blind(context)
        context.pour(map_variable.read(io))
        return self.fill(context)

    def get_required_variables_blind(self,context):
        return MapVariable({})

    def fill_return_value(self, context):
        pass

    def fill(self,context):
        return ValueHolder.get_new_value_holder_for(self.fill_return_value(context))

    def get_required_variables(self, context, io):
        if io is None:
            return self.get_required_variables_blind(self, context)
        return MapVariable({})

