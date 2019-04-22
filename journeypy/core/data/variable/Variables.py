class Readable(object):
    def read(self, io):
        pass


class ValueHolderVariable(Readable):
    valueHolderClass = None

    def __init__(self, value_holder_class):
        self.valueHolderClass = value_holder_class

    def read(self, io):
        io.writer.write_string(" of type String\n")
        return io.reader.read(self.valueHolderClass).value


class MapVariable(Readable):
    variable_map = {}

    def __init__(self, variable_map):
        self.variable_map = variable_map

    def read(self, io):
        data_map = {}
        for key in self.variable_map:
            io.writer.write_string("Please provide value for " + key)
            data_map[key] = self.variable_map[key].read(io)

        return data_map
